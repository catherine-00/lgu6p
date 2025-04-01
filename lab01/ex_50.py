import random
class Linear:
    def __init__(self, in_feature, out_feature):
        #random.random()
        #in_feature = 3 , out_feature = 2
        self.weight = [] #in_feature행, out_feature열
        self.bias = [] #(out_feature개)
      
               
        # W 행렬 만들기.
        for r in range(in_feature): # row = 0,1,2
            row = []
            for c in range(out_feature)  : # col = 0,1
                num = int(random.randrange(50))
                row.append(num)
            self.weight.append(row)
        print("\nself.weight : ", self.weight)


        #bias 행렬 만들기.
        for b in range(out_feature):
            num = int(random.randrange(50))
            self.bias.append(num)
        print("\nself.bias : ",self.bias)
   

    def matmul(self,A,B):
        #행렬곱 A, B를 해서
        #결과 행렬 C를 반환
        

        row = len(A)
        col = len(B[0])
        C = [] #A*B

        for i in range(row):
            temp = []
            for j in range(col):
                temp.append(0)
            C.append(temp)
        # C = [[0,0],
        #      [0,0],
        #      [0,0]]

        for i in range(len(A)):
            for j in range(len(B[0])):
                # A의 i행과 B의 j행을 내적
                for k in range(len(A[0])):
                    C[i][j] += A[i][k] * B[k][j]
        
        
        return C
        

    def forward(self, x) :
        #x 행렬곱 self.weight + self.bias
        Z = self.matmul(x,linear.weight)
        
    
        

        for r in range(len(Z)): #0,1
            for y in range(len(self.bias)): #0,1
                Z[r][y] = Z[r][y] + self.bias[y]

    
                
        return Z
        






linear = Linear(3,2)
x = [[1,2,3], 
     [4,5,6]]
linear.matmul(x,linear.weight)

print("\nY : ",linear.forward(x)) # 결과는 2행 2열로 나오면 됨.

print("====================================")

import numpy as np

x_np = np.array(x)
W_np = np.array(linear.weight)
b_np = np.array(linear.bias)

y_np = np.dot(x_np, W_np) + b_np
print(y_np)

'''
3행 2열의 self.weight를 random으로 만듦.



'''
