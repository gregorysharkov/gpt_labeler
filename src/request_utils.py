'''stores helper functions to send requests to open ai'''
import os
from typing import Dict

import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

SYSTEM_PROMT = '''You will be provided with a review. 
You will be required to answer several questions.
The format of an answer to each question should be a string with the format
'<numeric answer>~<comments>'
Comments should not be longer than 100 characters.
If multiple questions are asked the answer should contain as many lines as questions, separated by "\n"
No additional text is required, just answers
Questions to be answered:
Question 1. How satisfied was the post author about their stay in the hotel? Answer from 1 to 10, where 10 is the highest satisfaction.
Question 2. Did the authors of the post report any small talk with the receptionist/hotel clerk? Answer 1 for yes, 0 for no, None for unknown
'''

def generate_system_message() -> Dict:
    '''generates general instruction from the system'''

    return {
        'role': 'system',
        'content': SYSTEM_PROMT,
    }


def generate_user_message(review: str) -> Dict:
    '''generates a promt from user'''

    return {
        'role': 'user',
        'content': review,
    }


def generate_response(review: str):
    '''sesnds request to openai'''

    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            generate_system_message(),
            generate_user_message(review),
        ],
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )