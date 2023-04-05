def solution(n, arr1, arr2):
    temp = []
    for a, b in zip(arr1, arr2):
        map1 = format(a, 'b').zfill(n)
        map2 = format(b, 'b').zfill(n)

        temp.append((map1, map2))

    answer = []
    for maps in temp:
        treasure = ''
        for i in range(n):
            if maps[0][i] == '0' and maps[1][i] == '0':
                treasure += ' '
            else:
                treasure += '#'
        answer.append(treasure)

    return answer

# Solution


def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer


"""
importance knowing bitwise operator for this solution...

This line is performing a bitwise OR operation between two integers i and j,
and then converting the resulting integer to a binary string.

Let's break it down step by step:

i | j: The | operator is a bitwise OR operator,
whitch performs the OR operation on each corresponding pair of bits in the binary representation of i and j.
For example, if i is 0b1101 (which is 13 in decimal) and j is 0b1010 (which is 10 in decimal),
then i | j is 0b1111 (which is 15 in decimal). The | operator returns the result of this operaion as a new integer.

bin(i | j): The bin() function in Python converts an integer to a binary string.
When applied to the result of i | j, this returns a binary string representing the binary value of the result.
For example, if i is 0b1101 and j is 0b1010, then i | j is 0b1111, and bin(i | j) is the string "0b1111".

[2:]: Finally, the [2:] slice is used to remove the first two characters of the binary string,
which are always "0b". This leaves only the binary digits themselves.
For example, if i is 0b1101 and j is 0b1010, then i | j is 0b1111, and bin(i | j) is the string "0b1111".
Applying the [2:] slice to this string results in the string "1111",
which is the binary representation of i | j with the leading "0b" removed.

Finally, the resulting binary string is assigned to the variable a12
"""
