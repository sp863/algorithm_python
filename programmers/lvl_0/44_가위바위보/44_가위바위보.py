def solution(rsp):
    rspMap = {
        '2': '0',
        '0': '5',
        '5': '2'
    }

    return ''.join(rspMap[result] for result in rsp)

# Solution
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)