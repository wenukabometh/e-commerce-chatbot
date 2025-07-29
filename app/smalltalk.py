from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_MODEL = os.getenv("GROQ_MODEL")

client_smalltalk = Groq()

prompt = '''
    You are a helpful assistant built to assist with day to day life questions that people ask. You have to asnwer to that question. Refer the examples given below. 

    QUESTION: Hi, how are you?
    ANSWER: I'm doing great, thanks! How about you?

    QUESTION: "What are you up to?
    ANSWER": Just here to help you out. What’s on your mind?
'''

def talk(question):
    chat_completion = client_smalltalk.chat.completions.create(
        messages=[
            {
                'role': 'system',
                'content': prompt,
            },

            {
                'role': 'user',
                'content': question,
            }
        ],

        model=os.environ['GROQ_MODEL'],
        temperature=0.2
    )

    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    question = "I want to who is salmaan khan"
    response = talk(question)
    print(response)