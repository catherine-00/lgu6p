# # ex_str.py

# s = "Hello Python"
# print(s)

# s = 'Hello Python'
# print(s)

# s = "Hello \"EASY\" Python"
# print(s)

# s = 'Hello "EASY" Python'
# print(s)

# s = 'Hello,\n "EASY" Python'
# print(s)
# print(type(s))

# s = """Hello,
#        "EASY" Python
# """
# print(s)

# ############################
# # F-string
# ############################
# a = 10.0
# b = 20.0
# c = a * b
# # print('c:', c, 'SUCCESS')
# # print(f"c: {c} SUCCESS")
# print(f"{a1:5.2f} x {b:5.2f} = {c:.3f}")


# d = 5.2
# e = 21.234
# f = d * e
# print(f"{d:5.2f} x {e:5.2f} = {f:.3f}")

# a = "hello"
# print(f"{a:_^15}")



s = 'python,python'
print(type(s))

#count():해당되는 문자가 몇 개 있는지
print(s.count('python')) 

#find() : 처음 만나는 t의 인덱스. 없으면 -1이 출력됨.
print(s.find('t'))

#replace() : 바꾸기. 결과를 되돌려줄 뿐이지 값이 바뀌지는 않는다.
print(s.replace('python','PYTHON'))

#split() :특정 값을 기준으로 문자열 나눔. 리스트로 반환됨. 기본값은 space
print(s.split(','))

#join()
L = ['python','java','c++']
print(','.join(L)) #콤마를 이용해서 L을 join시켜라.문자열 상태로 쓰기

#strip()
s = '' \
'@<python>!'
print(f'|{s.strip("<>@!")}|')

#isdigit() , isalpha(), isalnum() : 결과는 True, False로 나옴.
s = '123a'
print(s.isdigit())#숫자로 바꿀 수 있는지

print(s.isalpha()) #알파벳인지

print(s.isalnum())#숫자와 알파벳만으로 이루어져 있는지.

#upper(), lower() : 대문자, 소문자로 바꾸기


