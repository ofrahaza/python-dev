# dictionaries
def wordsCountInPhrase():
    inp = input('Enter phrase: ')

    splitList = inp.split()
    dic = dict()

    print(f'Total words count = {len(splitList)}')

    for w in splitList:
        if w in dic.keys():
            dic[w] = dic[w] + 1
        else:
            dic[w] = 1

    print(f'Dictionary = {dic}')


wordsCountInPhrase()