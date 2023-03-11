def solution(my_string):
    unique = list(set(list(my_string)))
    answer = [''] * len(my_string)

    for target in unique:
        answer[my_string.index(target)] = target

    final = ''
    if ' ' in my_string:
        count = 0
        for letter in answer:
            if letter == ' ' and count >= 1:
                continue
            elif letter == ' ' and count == 0:
                final += letter
                count += 1
            else:
                final += letter
            print(final)
    else:
        for letter in answer:
            final += letter

    return final


# Solution
def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer+=i
    return answer