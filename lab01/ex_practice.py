# A =[[1,2,3],[4,5,6],[7,8,9]]
# A_square = [0,0,0]


# for i in range (len(A)):
#     A1=[]
#     for j in range(len(A[0])):
#         A1.append(A[i][j] *2)
#         A_square[i] = A1
#     print(A_square[i])

# print(A_square)

# print("===================================")


# A1=[]
# for row in A:
#     temp=[]
#     for a in row:
#         temp.append(a*2)
#     print(temp)
#     A1.append(temp)

# print(A1)

a= [1,2,3,4]
b = [4,5,6,7]
c=[]
total = 0
for i in range(len(a)):
    total += (a[i]*b[i])
    print(f'원소 곱 : {a[i]*b[i]}, total : {total}')
c.append(total)
print(c)