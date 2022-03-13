# Распознавание по определенному количеству схожих тегов, с использование коэффицента Жаккара.
# Допускается определнный процент ошибок в тегах.

from typing import List
from answers import *
from jakkardsCoefficent import calculateStringsJakkardsCoefficent


def MIN_SIMILAR_TAGS_COUNT() -> int:
    return 1


def MIN_TAG_JAKKARDS_COEFFICENT():
    return 0.5


def recognizeAnswer(question : str, answers : List[Answer]) -> Answer:
    questionTags = getTagsByText(question)
    suitableAnswer = None
    suitableAnswerSimilarTagsCount = MIN_SIMILAR_TAGS_COUNT()

    for a in answers:
        answerTags = a.getTags()
        similarTagsCount = 0
        for questionTag in questionTags:
            for answerTag in answerTags:
                if calculateStringsJakkardsCoefficent(questionTag, answerTag) > MIN_TAG_JAKKARDS_COEFFICENT():
                    similarTagsCount += 1
        if similarTagsCount >= suitableAnswerSimilarTagsCount:
            suitableAnswer = a
            suitableAnswerSimilarTagsCount = similarTagsCount

    return suitableAnswer