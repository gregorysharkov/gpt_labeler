'''contains functions for html representation of question information'''

from typing import Dict

from src.question import Answer, Question

# def get_question_html(question: Question) -> str:
#     '''represents a question'''

#     return f'<p class="question">{question.short_instruction}</p>'


# def get_answer_html(answer: Answer) -> str:
#     '''represents an answer'''

#     return f'<p>Numeric answer: {answer.numeric_answer}</p>' +\
#            f'<p>Comment: {answer.comment }</p>'

def get_complete_representation(question: Question, answer: Answer) -> Dict:
    '''combine question and answer representation'''

    return {
        'short_question': question.short_instruction,
        'numeric_answer': answer.numeric_answer,
        'comment': answer.comment,
    }
