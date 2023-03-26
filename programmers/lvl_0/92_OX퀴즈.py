def getResult(prob):
    split_prob = prob.split(' = ')
    result = split_prob[1]
    calc = split_prob[0]

    if '+' in calc:
        nums = calc.split(' + ')
        return 'O' if int(nums[0]) + int(nums[1]) == int(result) else 'X'
    else:
        nums = calc.split(' - ')
        return 'O' if int(nums[0]) - int(nums[1]) == int(result) else 'X'



def solution(quiz):
    return [getResult(prob) for prob in quiz]

# Solution
def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]

def solution(quiz):
    answer = []
    for q in quiz:
        L,R = q.split(' = ')
        a,op,b = L.split()
        if op=='+':
            result = 'O' if int(a)+int(b)==int(R) else 'X'
            answer.append(result)
        else:
            result = 'O' if int(a)-int(b)==int(R) else 'X'
            answer.append(result)
    return answer