from random import shuffle
from html import unescape

class QuizController:
    def __init__(self):
        self.question_number = 0
        self.score = 0
        self.is_bool = False
        self.choices = {letter: "" for letter in "abcd"}

    @staticmethod
    def user_input_checker(valid_answers, other_choices):
        """Check if user input is valid against given answers and choices."""
        valid_set = {ans.lower() for ans in valid_answers + other_choices} | {"true", "false", "a", "b", "c", "d"}
        while True:
            user_input = input("Your answer: ").strip().lower()
            if user_input in valid_set:
                return user_input
            print("Please answer with one of the available choices.")

    def question_type_checker(self, question):
        """Detect and print the type of question."""
        self.is_bool = (question.question_type != "multiple")
        q_type = "True/False" if self.is_bool else "Multiple choice"
        print(f"******** This is a {q_type} question ********")

    def print_choices(self, other_choices, correct_answer):
        """Show shuffled choices depending on question type."""
        if self.is_bool:
            print("(True or False)")
            return
        choices = other_choices + [correct_answer]
        shuffle(choices)
        for letter, choice in zip(self.choices.keys(), choices):
            self.choices[letter] = choice
            print(f"{letter.upper()}. {choice}")

    def user_input(self, correct_answer, other_choices):
        """Assess the user's answer."""
        valid_answers = [correct_answer.lower()] + [letter for letter, option in self.choices.items() if option == correct_answer]
        user_answer = self.user_input_checker(valid_answers, other_choices)

        if user_answer in valid_answers:
            self.score += 1
            print("You're correct!")
        else:
            if not self.is_bool:
                for letter, option in self.choices.items():
                    if option == correct_answer:
                        print(f"Sorry, wrong answer. The correct answer is: {letter.upper()}. {option}")
                        break
            else:
                print(f"Sorry, wrong answer. The correct answer is: {correct_answer}")
        self.question_number += 1

    def print_current_score(self):
        print(f"Your current score: {self.score}/{self.question_number}")

    def start_quiz(self, list_of_questions):
        """Run the quiz over a list of QuestionModel objects."""
        for question in list_of_questions:
            # print(f"The correct answer is: {question.question_answer}")
            self.is_bool = False
            self.question_type_checker(question)
            print(unescape(question.question))
            self.print_choices(question.other_choices, question.question_answer)
            self.user_input(question.question_answer, question.other_choices)
            self.print_current_score()
            input("Press Enter for the next question...")

        print(f"You completed the quiz! Final score: {self.score}/{self.question_number}")
