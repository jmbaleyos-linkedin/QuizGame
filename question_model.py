from html import unescape

class QuestionModel:
    def __init__(self, question_list):
        self.question_type = question_list["type"]
        self.question_difficulty = question_list["difficulty"]
        self.question_category = question_list["category"]
        self.question = unescape(question_list["question"])
        self.question_answer = unescape(question_list["correct_answer"])
        self.other_choices = self.deep_unescape(question_list["incorrect_answers"])

    def deep_unescape(self, data):
        """Converts the JSON string to unescaped version, in order to eliminate any symbols code."""
        if isinstance(data, str):
            return unescape(data)
        elif isinstance(data, dict):
            return {k: self.deep_unescape(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [self.deep_unescape(item) for item in data]
        else:
            return data