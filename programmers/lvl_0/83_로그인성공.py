def solution(id_pw, db):
    for data in db:
        if data[0] == id_pw[0] and data[1] == id_pw[1]:
            return "login"
        if data[0] == id_pw[0] and data[1] != id_pw[1]:
            return "wrong pw"
    return "fail"

# Solution
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"

def solution(id_pw, db):
    dic = dict(db)
    if dic.get(id_pw[0],-1) == id_pw[1]:
        return "login"
    elif dic.get(id_pw[0],-1) == -1:
        return "fail"
    else:
        return "wrong pw"
    

def solution1(chicken):
    ordered = 0 # 108 118
    coupons = chicken # 10
    
    while coupons > 0:
        ordered += (coupons // 10)
        coupons 
        

    
    return ordered

solution1(100)