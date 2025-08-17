from quizutils.QuestionsHub import QuestionsHub


class Quiz:

    def __init__(
        self,
        questions_type: str,
        no_of_questions: int,
        score: int = 0,
        is_random: bool = False,
    ):
        self.questions_type = questions_type
        self.no_of_questions = no_of_questions
        self.score = score
        self.is_random = is_random

    def __str__(self) -> str:
        return "Quiz Instance created"

    def __repr__(self) -> str:
        return f"Quiz(name={self.questions_type},noOfQuestions={self.no_of_questions},isRandom={self.is_random})"

    @staticmethod
    def print_results(current_score: int, questions_count: int) -> None:
        if current_score == questions_count:
            print(
                f"End of Quiz. Your Passed and your scored {current_score}/{questions_count}"
            )
        else:
            print(
                f"End of Quiz. Your Failed and your scored {current_score}/{questions_count}"
            )

    def startQuiz(self) -> None:
        if self.no_of_questions == 0:
            print("There are no questions for this Quiz")
            return
        questions_container = QuestionsHub(self.questions_type, self.no_of_questions)
        answers = []
        for i, question in enumerate(questions_container.generate_questions()):
            question_text, answer = question.split("|")
            answer_text = answer.split(":", 1)[1].strip()
            answers.append(input(question_text))
            if answers[i] == answer_text:
                self.score += 1
        Quiz.print_results(self.score, self.no_of_questions)
