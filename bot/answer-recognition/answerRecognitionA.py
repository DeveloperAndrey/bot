# Распознавание по схожим наборам букв, с использованием коэффицента Жаккара.

from typing import List
from answers import Answer
from jakkardsCoefficent import calculateStringsJakkardsCoefficent


def MIN_SUITABLE_ANSWER_JAKKARDS_COEFFICENT() -> float:
    return 0.6


def recognizeAnswer(question : str, answers : List[Answer]) -> Answer:
    suitableAnswer = None
    suitableAnswerCoefficent = MIN_SUITABLE_ANSWER_JAKKARDS_COEFFICENT()

    for a in answers:
        for q in a.questions:
            coefficent = calculateStringsJakkardsCoefficent(q, question)
            if coefficent > suitableAnswerCoefficent:
                suitableAnswer = a
                suitableAnswerCoefficent = coefficent

    return suitableAnswer