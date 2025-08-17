from pathlib import Path


class QuestionsHub:
    no_of_instances: int = 0

    def __init__(self, question_type: str, no_of_questions: int) -> None:
        self.question_type = question_type
        self.no_of_questions = no_of_questions
        __class__.no_of_instances += 1

    @classmethod
    def get_instance_count(cls) -> int:
        return cls.no_of_instances

    def __str__(self) -> str:
        return f"Questions Bundle processed"

    def __repr__(self) -> str:
        return f"QuestionsHub(questionsType={self.question_type},noOfQuestions={self.no_of_questions})"

    def generate_questions(self) -> list[str]:
        file_path = Path.cwd() / "data" / "moviesQuestions.txt"
        try:
            with file_path.open("r", encoding="utf-8") as file:
                questions_list = [line.strip() for line in file.readlines()]
                return questions_list[0 : self.no_of_questions]
        except FileNotFoundError as error:
            print(error)
            return []
