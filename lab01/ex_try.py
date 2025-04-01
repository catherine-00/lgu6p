# ex_44.py

# 연산자와 해당하는 람다 함수를 딕셔너리에 직접 매핑
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y 
}

# 두 수와 연산자를 사용자로부터 입력받고
# 입력된 연산을 operations를 이용하여 수행하기
# print( operations['+'](10,2) )




try :
    x = float(input("x: "))
    y = float(input("y: "))
    op = input("연산자(+, -, *, /): ")

    # if op in operations.keys(): #  ['+', '-', '*', '/']:
    result = operations[op](x, y)
    print(result)
   
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")
    print(e)
    

except ValueError as e:
    print("숫자만 입력 가능합니다.")
    print(e)

except KeyError as e:
    print("잘못된 연산자입니다.")
    print(e)

except exception as e:
    print("알 수 없는 오류가 발생했습니다.")
    print(e)

finally:
    print("프로그램 종료.")
