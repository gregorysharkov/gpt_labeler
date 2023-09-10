'''main application entry point'''

import json
from typing import Dict, List

from flask import Flask, redirect, render_template, request, url_for

# from src.output_elements.question import get_complete_representation
from src.question import Answer, Question
from src.request_utils import generate_response

QUESTIONS = [
    Question(
        number=1,
        promt='How satisfied was the post author about their stay in the hotel?',
        evaluation_instruction='Answer from 1 to 10, where 10 is the highest satisfaction.'
    ),
    Question(
        number= 2,
        promt='Did the authors of the post report any interaction with the personnel?',
        evaluation_instruction='Answer 1 for yes, 0 for no, None for unknown'
    ),
]

app = Flask(__name__)

@app.route("/", methods=("GET", "POST"))
def index():
    '''default entry point to the application'''
    if request.method == "POST":
        original_review = request.form.get('review')
        answer_list = process_review(original_review)
        print(f'--------------------answer list inside post redirection: {answer_list}')
        new_url = url_for(
            'index',
            original_review=original_review,
            answer_list=answer_list,
        )
        return redirect(new_url)

    original_review = request.args.get('original_review')
    answer_list = parse_get_list(
        request.args.getlist('answer_list')
    )
    print(f'--------------------answer list inside get instruction: {answer_list}')

    rendered_template = render_template(
        "index.html",
        original_review=original_review,
        answer_list=answer_list,
    )
    return rendered_template


def parse_get_list(answer_list: List | None) -> List[Dict] | None:
    '''converts list of strings from get request into a list of dictionaries'''

    if not answer_list:
        return None
    
    return [
        json.loads(answer)
        for answer in answer_list
    ]


def get_complete_representation(question: Question, answer: Answer) -> Dict:
    '''combine question and answer representation'''

    return {
        "short_question": question.short_instruction,
        "numeric_answer": answer.numeric_answer,
        "comment": answer.comment,
    }


def process_review(review: str | None) -> List[Dict]:
    '''function processes review'''
    if review is None:
        return None
    response = generate_response(review, QUESTIONS)
    response_text = response['choices'][0]['message'].content
    answers = [process_single_response(promt) for promt in response_text.split(';')]

    # temprorary solution for debug
    # answers = [
    #     Answer(1, 'Some answer to the first question'),
    #     Answer(2, 'Some answer to the second question'),
    # ]

    answer_list = [
        json.dumps(
            {
                'short_question': question.short_instruction,
                'numeric_answer': answer.numeric_answer,
                'comment': answer.comment,
            }
        )
        for question, answer in zip(QUESTIONS, answers)
    ]

    return answer_list



def process_single_response(promt) -> Answer:
    return Answer(*promt.split('~'))


if __name__ == "__main__":
    app.run()