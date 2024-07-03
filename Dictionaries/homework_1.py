import math

listFromRange = list(range(5, 15))

newList = []

for i in range(len(listFromRange)):
    if i % 2 == 0:
        newList.append(listFromRange[i])

sumResult = sum(newList)
sumProd = math.prod(newList)
resultList = newList.copy()
resultList.append(sumResult)
resultList.append(sumProd)

resultList.sort(reverse=True)

print('='.join([str(x) for x in resultList]))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 5, 9, -7, -10]

print(', '.join([str(x) for x in a if x < 5]))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 11]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 34, 11, 12, 13]

c = list(set([value for value in a if value in b]))
c.sort()

print(', '.join([str(value) for value in c]))

s = 'kafka python course stack flow dict list python stack course star product star product analytics flow star kafka stack flow ython list set ist fit predict dict list python ourse ython ourse star product ist fit predict analytics kafka stack flow product ist fit predict analytics star flow dict flow list python course stack flow dict list python stack course'

d = 'fff aaa fff fff aaa aaa'


def freq(st):
    ls = st.split()
    dc = {w: ls.count(w) for w in set(ls)}
    m = max(dc.values())
    maxList = [k for k in dc if dc[k] == m]
    maxList.sort()
    return maxList[0]


print(freq(s))
print(freq(d))

names = ['igor', 'dasha', 'martin', 'vladimir', 'rishat', 'maria', 'marat', 'petr', 'dima', 'polina', 'katya', 'elena']

occupations = ['smm', 'developer', 'analyst', 'president', 'analyst', 'ceo', 'customer development', 'founder',
               'developer', 'ml engineer', 'product manager', 'cmo']

tuples = zip(names, occupations)
dictNamesOcc = dict(tuples)

print(dictNamesOcc['maria'])

dict1 = {1: 10, 2: 20, 3901: 11, 384: 13, 8489: 1, 48: 10}

dict2 = {3: 30, 4: 40, 93: 12, 91: 41, 95: 1, 841: 11, 584: 11}

dict3 = {5: 50, 6: 60, 9: 90, 3: 13, 7: 11}

mergedDictionary = {**dict1, **dict2, **dict3}

print(mergedDictionary)
print(len(mergedDictionary))

ls = list(mergedDictionary.values())
dc = {w: ls.count(w) for w in set(ls)}
m = max(dc.values())
maxList = [k for k in dc if dc[k] == m]
maxList.sort()

print(maxList[0])

given_string = 'Python Star Course for beginners and experts for data science and analytics without sql with code'

formattedString = given_string.replace(" ", "").replace(",", "")

print(formattedString)

ls = list(formattedString)
dc = {w: ls.count(w) for w in set(ls)}
sortedByValues = dict(sorted(dc.items(), key=lambda x:x[1]))

res = list(sortedByValues.keys())
#PSCbgxpq
print("".join(res[0:8]))