from dataclasses import dataclass


@dataclass
class Answer():
    '''responsible for storing and representing gpt result'''
    numeric_answer: object
    comment: str

@dataclass
class Question():
    '''responsible for handling question operations'''
    number: int
    promt: str
    evaluation_instruction: str

    @property
    def instruction(self) -> str:
        '''returns instruction for openai object'''

        return f"Question{self.number}: {self.promt} {self.evaluation_instruction}"

    @property
    def short_instruction(self) -> str:
        '''returns short instruction for output'''

        return f"Question{self.number}. {self.promt}"
