# Распознавание по проценту схожих тегов, с использованием коэффицента Жаккара.
# Допускается определнный процент ошибок в тегах.

from typing import List
from jakkardsCoefficent import calculateJakkardsCoefficent
from jakkardsCoefficent import calculateStringsJakkardsCoefficent
from answers import *


def MIN_TAG_JAKKARDS_COEFFICENT():
    return 0.5


def MIN_SUITABLE_ANSWER_JAKKARDS_COEFFICENT() -> float:
    return 0.7


def recognizeAnswer(question : str, answers : List[Answer]) -> Answer:
    questionTags = getTagsByText(question)
    suitableAnswer = None
    suitableAnswerJakkardsCoefficent = MIN_SUITABLE_ANSWER_JAKKARDS_COEFFICENT()

    for a in answers:
        answerTags = a.getTags()
        similarTagsCount = 0

        for questionTag in questionTags:
            for answerTag in answerTags:
                if calculateStringsJakkardsCoefficent(questionTag, answerTag) > MIN_TAG_JAKKARDS_COEFFICENT():
                    similarTagsCount += 1

        answerJakkardsCoefficent = calculateJakkardsCoefficent(len(questionTags), len(answerTags), similarTagsCount)

        if answerJakkardsCoefficent >= suitableAnswerJakkardsCoefficent:
            suitableAnswer = a
            suitableAnswerJakkardsCoefficent = answerJakkardsCoefficent

    return suitableAnswer