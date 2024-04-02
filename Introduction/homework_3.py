print('Enter some numbers in one line')

raw_input = input()

splitted_input = raw_input.split()  # split on any whitespace character (including \n \r \t \f and spaces) string numbers into array

parsed_input = list()  # create new empty list

for raw in splitted_input:
    parsed_input.append(int(raw))  # cast string numbers to int type and append them to new list

parsed_input.sort()  # sort numbers in list

print(f' your result: {parsed_input}')  # print sorted list
