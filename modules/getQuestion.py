from random import randint


def getQuestion(data):
    data_len = len(data)
    index = randint(0, data_len - 1)
    return index
