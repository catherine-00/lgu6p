L = [1,2,3,4,5]

for i in range(len(L)):
    print('index : ', i)
    print('L[i]:', L[i])
    print()

for j in L:
    print("j :",j)


D ={'a' : 100, 'B' :200, 'C':300}
# print("D.items : ", D.items())
# = dict_items([('a', 100), ('B', 200), ('C', 300)])
# 튜플이 날아온다. 튜플이 k,v에 (_,_)가 언패킹된다.

for k,v in D.items():
    print(k,v)

#while 옆에는 조건을 판단할 수 있는 것이면 다 된다. 
# True도 그 자체로 참이라서 가능한 것.
# while ():