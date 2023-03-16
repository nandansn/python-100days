from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def create_question_bank():
    question_bank = []
    for item in question_data:
        question = Question(item['text'],item["answer"])
        question_bank.append(question)

    return question_bank

question_bank = create_question_bank()

quiz_brain = QuizBrain(question_bank)
quiz_brain.question_answer()
