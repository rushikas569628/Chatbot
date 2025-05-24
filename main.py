
from openai import OpenAI

openai = OpenAI(
    api_key="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"
)
response = openai.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        #initially trying to set a behaviour
        {
            'role': 'system',
            'content': 'You are CEO of apple'
        },
        # “In the past, the assistant already said: ‘iPhone is awesome.’”
        {
            'role': 'assistant',
            'content': 'iphone is awesome'
        },
        # present prompt
        {
            'role': 'user',
            'content': 'in which year it is released?'
        }
    ]
)

print(response.choices[0].message.content)
print("                                     ")
print(response)