from re import split
from typing import List
from winreg import QueryInfoKey


def getTagsByText(text : str) -> List[str]:
    formatted = text
    formatted = formatted.replace("?", " ")
    formatted = formatted.replace(",", " ")
    formatted = formatted.replace(".", " ")
    formatted = formatted.replace("!", " ")
    return formatted.split()


class Answer:
    questions = List[str]
    

    def __init__(self, questions : List[str]) -> None:
        lowered = []
        for question in questions:
            lowered .append(question.lower())
        self.questions = lowered


    def getTags(self) -> List[str]:
        tags = []
        for question in self.questions:
            tags += getTagsByText(question)
        return tags


    def toString() -> str:
        pass


class StaticAnswer(Answer):
    answer : str = ""


    def __init__(self, questions : List[str], answer : str) -> None:
        super().__init__(questions)
        self.answer = answer


    def toString(self) -> str:
        return self.answer