

# def outer_function(msg):
#     def inner_function():
#         print(f"메시지: {msg}") # 외부 함수의 변수(msg) 사용
#     return inner_function

# closure = outer_function("안녕하세요!")
# closure() # 메시지: 안녕하세요!



import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs) #우리가 만든 함수의 리턴 값
        end_time = time.time()
        print(f"{func.__name__} 실행 시간: {end_time-start_time:.5f}초")
        return result
    return wrapper

@timing_decorator
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

# fibo_num_gen = timing_decorator(fibo_num_gen)

@timing_decorator
def fibonacci_deco(n):
    return [_ for _ in fibo_num_gen(n)]








