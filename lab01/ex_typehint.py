
# def add(a,b):
#     '''
#     두 수 a,b를 더하는 함수
    
    
#     '''

#     return a+b

# help(add)


def mul(a: int ,b : int) -> int : 
    #a,b는 int여야 한다.리턴 값도
    #근데 int로 변환해주지는 않는다. 그냥 주석같은 느낌.
    return a*b

print(mul(3,4))
print(mul('3',4))