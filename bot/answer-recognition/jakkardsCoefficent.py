# Вычисление коэффицента Жаккара (коэффицент сходства)
# a - кол-во всех проверяемых единиц первого элемента
# b - кол-во всех проверяемых единиц второго элемента
# c - кол-во общих для первого и второго элементов едини


from typing import Dict


def calculateJakkardsCoefficent(a : int, b : int, c : int) -> float:
    return c / (a + b - c)


def getStringCharCounts(string : str) -> Dict[chr, int]:
    result = {}
    for c in string:
        if c in result:
            result[c] = result[c] + 1
        else:
            result[c] = 1
    return result


def getCharCountsIntersection(a : Dict[chr, int], b : Dict[chr, int]) -> Dict[chr, int]:
    result = {}
    for c in a:
        if c in b:
            if not(c in result):
                if a[c] > b[c]:
                    result[c] = b[c]
                else:
                    result[c] = a[c]
    return result


def getCharCount(charCounts : Dict[chr, int]) -> int:
    count = 0
    for c in charCounts:
        count += charCounts[c]
    return count


def calculateStringsJakkardsCoefficent(stringA : str, stringB : str) -> float:
    aCharCounts = getStringCharCounts(stringA)
    bCharCounts = getStringCharCounts(stringB)
    charCountsIntersection = getCharCountsIntersection(aCharCounts, bCharCounts)

    a = getCharCount(aCharCounts)
    b = getCharCount(bCharCounts)
    c = getCharCount(charCountsIntersection)

    return calculateJakkardsCoefficent(a, b, c)