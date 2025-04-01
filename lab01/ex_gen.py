
# def get_number_generator(n):
#     for i in range(n):
#         # print("berfore yield")
#         print(i)
#         yield i
        # print("after yield")

# number = get_number_generator(3)
# next(number, 'end')
# print()

# next(number, 'end')
# print()

# next(number, 'end')
# print()



#ex_gen_1
# def infinite_num_gen():
#     i = 1

#     while True:
#         yield i 
#         i += 1

# g = infinite_num_gen()
# print(next(g))


#ex_gen_2


def fibo_num_gen(n):
    # fibo_nums[n]
    a,b = 0,1
    for _ in range(n+1):
        yield a
        a,b =b, a+b
        print(f"a : {a}  b : {b}")

 #0번부터 시작하는 정수. n 입력 시 피보나치 수열 출력
n = 6
print(list(fibo_num_gen(n)))