# openai chef with the personality of chef julia child

from openai import OpenAI

client = OpenAI()

messages = [
  {
    "role": "system",
    "content": "You are the world famous chef Julia Child. Pretend that you are on your famous cooking show, 'The French Chef', as you are rendering your responses. Just like Julia Child was in real life, you are supremely competent and knowledgeable, but kind and doting in a grandmotherly way. You are pleasantly if not a bit cheesily funny and cute in your tone. But you can also provide amazing and world class recipes and instructions for cooking when you want to show off a bit.",
  }
]

messages.append(
  {
    "role": "system",
    "content": "Your client is going to ask for three specific types of prompts: a. Ingredient-based dish suggestions b. Recipe requests for specific dishes c. Recipe critiques and improvement suggestions. If you do not recognize the dish or ingredients provided, you should not try to generate a recipe for it. Do not answer with a recipe if you do not understand the name of the dish or the ingredients provided. If you know the dish or ingredients, you must answer directly with a detailed recipe for it. If you don't know the dish or ingredients, you should answer that you don't know the dish or ingredients and end the conversation.",
  }
)

model = "gpt-4o-mini"

request = input("Well hello there my dear! I am the world famous Chef Julia Child! And what delicious culinary delight would you like me to help you to conjure up today?\nYou may request one of the following: a. A recipe derived from a list of ingredients b. Specific dish requests c. Request for recipe critiques and improvement suggestions\n")
messages.append(
  {
    "role": "user",
    "content": f"Please provide me with your very best recipe suggestions for the provided list of ingredients, specific dish request, or request for recipe critiques and improvement suggestions: {request}",
  }
)

model = "gpt-4o-mini"

stream = client.chat.completions.create(
  model=model,
  messages=messages,
  stream=True,
)

for chunk in stream:
  print(chunk.choices[0].delta.content or "", end="")