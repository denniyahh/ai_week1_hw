import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def get_response(input_type, user_message):
    messages = []

    if input_type == "ingredient":
        # Prompt for suggesting dishes based on ingredients
        messages = [{
            "role": "system",
            "content": "You are an ancient Greek philosopher and herbalist turned chef. You specialize in Greek-inspired dishes using simple, earthy ingredients. When users provide ingredients, you suggest dish names inspired by the Greek gods but do not provide full recipes."
        }, {
            "role": "user",
            "content": f"Share a Greek-inspired dish name based on the following ingredients: {user_message}. If the ingredients are unfamiliar to you, respond with an ancient Greek saying about simplicity in life, and politely end the conversation."
        }]

    elif input_type == "dish":
        # Prompt for providing detailed recipes
        messages = [{
            "role": "system",
            "content": "You are an ancient Greek philosopher and herbalist turned chef. You specialize in Greek-inspired dishes, sharing recipes filled with rustic flavors and ancient wisdom. When users provide a dish name, provide a detailed recipe with philosophical wisdom woven into each step."
        }, {
            "role": "user",
            "content": f"Reveal the recipe and preparation steps for making {user_message} with an ancient Greek spirit. If the dish is unknown, reply with a proverb about humility in the pursuit of knowledge, and politely end the conversation."
        }]

    elif input_type == "recipe":
        # Prompt for critiquing recipes
        messages = [{
            "role": "system",
            "content": "You are an ancient Greek philosopher and herbalist turned chef. You specialize in Greek-inspired dishes and critique recipes with wisdom and a philosophical outlook. When critiquing, use poetic language and refer to ancient Greek principles."
        }, {
            "role": "user",
            "content": f"Critique the following recipe and suggest improvements: {user_message}. Remember to add a touch of poetic Greek wisdom to your critique."
        }]

    model = "gpt-4o-mini"
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    return "".join(collected_messages)


def main():
    print("Greetings, seeker of culinary wisdom! I am here to share flavors inspired by ancient Greece. Tell me of your ingredients, dishes, or recipes, and I shall guide you with the wisdom of the ancients.")
    while True:
        user_message = input("\nWhat guidance do you seek? (type 'exit' to quit):\n").strip()

        if user_message.lower() == "exit":
            print("Farewell, and may your meals bring you enlightenment!")
            break

        input_type = None
        if "ingredient" in user_message.lower():
            input_type = "ingredient"
        elif "dish" in user_message.lower():
            input_type = "dish"
        elif "recipe" in user_message.lower():
            input_type = "recipe"
        else:
            print("Alas, I can only guide you in the realm of ingredients, dishes, or recipes. Please try again.")
            continue

        user_detail = input(f"Ah, yes. Share the details of the {input_type} (type 'exit' to quit):\n").strip()

        if user_detail.lower() == "exit":
            print("Farewell, and may your meals bring you enlightenment!")
            break

        response = get_response(input_type, user_detail)
        print("\nOracle of Greek Cuisine:\n", response)


if __name__ == "__main__":
    main()
