import statistics
# import pprint

# pprint.pprint("{'d': 6}")

dict_1 = {
    'name': 'name_1',
    'age': 32,
    'gender': 'male'
}

dict_2 = {
    'name': 'name_2',
    'age': 17,
    'gender': 'male'
}

dict_3 = {
    'name': 'name_3',
    'age': 55,
    'gender': 'female'
}

dict_4 = {
    'name': 'name_4',
    'age': 17,
    'gender': 'male'
}

dict_5 = {
    'name': 'name_5',
    'age': 25,
    'gender': 'female'
}

dict_6 = {
    'name': 'name_6',
    'age': 42,
    'gender': 'female'
}

dict_7 = {
    'name': 'name_7',
    'age': 23,
    'gender': 'female'
}

dict_list = [dict_1, dict_2, dict_3, dict_4, dict_5, dict_6, dict_7]


def addition(n):
    return n['age']


def get_avg_age(gender):
    list_same_gender = []

    for i in dict_list:
        if i['gender'] == gender:
            list_same_gender.append(i['age'])

    return statistics.mean(list_same_gender)


print(get_avg_age('male'))
