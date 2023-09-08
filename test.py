import os

import openai

openai.api_key = ("key")

openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)


print(completion.choices[0].message)