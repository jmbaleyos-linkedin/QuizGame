from data import GetData
from question_model import QuestionModel
from quiz_controller import QuizController

data_exist = True
requested_data = GetData()

if requested_data.questions_data is None:
    data_exist = False

if data_exist:
    questions_bank = []
    for question in requested_data.questions_data["results"]:
        questions_bank.append(QuestionModel(question))
    start_quiz = QuizController()
    start_quiz.start_quiz(questions_bank)