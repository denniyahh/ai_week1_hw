import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def get_response(input_type, user_message):
    messages = []

    if input_type == "ingredient":
        # Prompt for suggesting dishes
        messages = [{
            "role": "system",
            "content": "You are a former international football (soccer) player turned experienced chef. You specialize in dishes from Trinidad and Tobago and the Caribbean. When users provide ingredients, you suggest dish names but do not provide full recipes."
        }, {
            "role": "user",
            "content": f"Suggest a dish name based on the following ingredients: {user_message}. If the ingredients are not typically found in Trinidad and Tobago or the Caribbean, you should answer that you don't know about those ingredients making some football reference about fouling and end the conversation"
        }]

    elif input_type == "dish":
        # Prompt for detailed recipes
        messages = [{
            "role": "system",
            "content": "You are a former international football (soccer) player turned experienced chef. You specialize in dishes from Trinidad and Tobago and the Caribbean. When users provide a dish name, you provide a detailed recipe with preparation steps."
        }, {
            "role": "user",
            "content": f"Suggest me a detailed recipe and the preparation steps for making {user_message}. If you don't know the dish, you should answer that you don't know the dish making some football reference about fouling and end the conversation"
        }]

    elif input_type == "recipe":
        # Prompt for critiquing recipes
        messages = [{
            "role": "system",
            "content": "You are a former international football (soccer) player turned experienced chef. You specialize in dishes from Trinidad and Tobago and the Caribbean. When users provide a recipe, you offer a constructive critique with suggested improvements."
        }, {
            "role": "user",
            "content": f"Critique the following recipe and suggest improvements: {user_message}. Remember to critique with sass and Caribbean attitude and you football background, puns and references"
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
    print("Welcome, man! Great to have you here! I’m not just here to serve up a meal; I’m here to share the flavours of the islands! If you’re curious about ingredients, dish names, or even how to make these recipes yourself, just ask.")
    while True:
        user_message = input("\nTell me what you need help with today (type 'exit' to quit):\n").strip()

        if user_message.lower() == "exit":
            print("Goodbye! Have a great day!")
            break

        input_type = None
        if "ingredient" in user_message.lower():
            input_type = "ingredient"
        elif "dish" in user_message.lower():
            input_type = "dish"
        elif "recipe" in user_message.lower():
            input_type = "recipe"
        else:
            print("Sorry, I can only help with ingredients, dish names, or recipes. Please try again.")
            continue

        user_detail = input(f"Great! Please provide the details for the {input_type} (type 'exit' to quit):\n").strip()

        if user_detail.lower() == "exit":
            print("Goodbye! Have a great day!")
            break

        response = get_response(input_type, user_detail)
        print("\nTT TasteMaker GPT:\n", response)


if __name__ == "__main__":
    main()
