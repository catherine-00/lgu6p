user_id = '1234'
user_pw = '1234'
AUTH = False

def login() :
    
    i = 0
    global AUTH

    
    while i == 0 :
        id = input("아이디 입력 : ")
        if user_id == id :
            j = 0
            while j == 0 :
                pw = input("비밀번호 입력 : ")
                if user_pw == pw:
                    print("로그인 성공")
                    AUTH = True
                    i = 1
                    j = 1

                else:
                    print("[!] 비밀번호가 틀렸습니다.")
            

        else :
            print("[!] 아이디가 틀렸습니다.")
    
    return AUTH


# 사용 승인 체크 데코레이터
def auth_required(func):
    def wrapper(*args, **kwargs):
        #로그인 인증
        global AUTH

        if AUTH == True :
            print("접근 승인")
            result = func(*args, **kwargs)
            
        else:
            result = print("[!]접근 권한이 없습니다.")
            
        
        return result
    return wrapper

        

# 이 함수에 완성된 데코레이터를 적용해주세요.
@auth_required
def order_list():
    print("*********************")
    print("구매 리스트 출력")
    print("만두, 아이스크림, 콜라")
    print("*********************")

# 이 함수에 완성된 데코레이터를 적용해주세요.
@auth_required
def return_list():
    print("*********************")
    print("반품 리스트 출력")
    print("커피, 책")
    print("*********************")

# 이 함수에는 데코레이터를 적용하지 마세요.
def recommend_list():
    print("*********************")
    print("추천 목록 출력")
    print("참치, 라면, 피자")
    print("*********************")

while True:
    print("============================")
    print("[0] : 로그인")
    print("[1] : 구매 리스트")
    print("[2] : 교환 반품 리스트")
    print("[3] : 오늘의 추천 상품")
    c = input("메뉴 선택: ")

    if c == "1":
        order_list()
    elif c == "2":
        return_list()
    elif c == "3":
        recommend_list()
    elif c == "0":
        login()
    else:
        break


