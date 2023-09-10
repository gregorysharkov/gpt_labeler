'''stores helper functions to send requests to open ai'''
import os
from typing import Dict, List

import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

from src.question import Question

SYSTEM_PROMT = '''You will be provided with a review please answer
Answer format '<numeric answer>~<your comments why this answer>'
Your comments for each answer should be less than 100 characters.
No additional text is required, different answers have to be separated by ';'
Number of answers should always be equal to the number of questions
Questions:
'''
# Question 1. How satisfied was the post author about their stay in the hotel? Answer from 1 to 10, where 10 is the highest satisfaction.
# Question 2. Did the authors of the post report any small talk with the receptionist/hotel clerk? Answer 1 for yes, 0 for no, None for unknown

def generate_system_message(questions: List[Question]) -> Dict:
    '''generates general instruction from the system'''

    promt = SYSTEM_PROMT + r'\n'.join(question.instruction for question in questions)
    return {
        'role': 'system',
        'content': promt,
    }


def generate_user_message(review: str) -> Dict:
    '''generates a promt from user'''

    return {
        'role': 'user',
        'content': review,
    }


def generate_response(review: str, questions: List[Question]):
    '''sesnds request to openai'''
    chat_object = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            generate_system_message(questions),
            generate_user_message(review),
        ],
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(chat_object)
    return chat_object
