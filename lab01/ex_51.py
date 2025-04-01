import ex_45


s = '1,2,3,4 5 6 7,8,9,10'
# input("평균을 구할 숫자를 입력(콤마 또는 공백으로 구분) : ")
# L = []
# lst=[]
# print(s)

# L = s.split(',')
# print(f'L : ',L)

# for i in L:
#     i = float(i)
#     lst.append(i)
# print(f"lst : {lst}")

# m = ex_45.mean(lst)
# print(f"평균 : {m}")

L = [ int(i) for i in s.replace(',',' ').split() ]
m = ex_45.mean(L)
print(m)
