def distance(codeA,codeB):
    if len(codeA) == len(codeB):
        return sum([codeA[i] != codeB[i] for i in range(0, len(codeA))])
    else:
        raise ValueError