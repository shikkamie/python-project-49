import random

description = "What number is missing in the progression?"


def generate_question():

    start = random.randint(2, 9)
    step = random.randint(3, 8)
    stop = start + step * 5
    lst = list(range(start, stop, step))
    tts = 0
    swap = ".."
    for i in lst:
        if i % 10 == 0:
            tts = i

    if tts == 0:
        rnd = random.randint(1, len(lst) - 1)
        swap, lst[rnd] = lst[rnd], swap
    else:
        for i in range(len(lst)):
            if lst[i] == tts:
                swap, lst[i] = lst[i], swap

    return str(lst), str(swap)
