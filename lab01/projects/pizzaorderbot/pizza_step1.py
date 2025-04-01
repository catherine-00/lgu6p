
def step1():
    print("빅데이터 피자 가게에 오신 것을 환영합니다.")



    while True:
        input_menu = input(
"""
피자를 선택하세요. 수량 추가를 위해 여러번 선택 가능합니다.
1. 페퍼로니 피자 (29,000원)
2. 스테이크 피자 (32,000원)
3. 시푸드 피자 (32,000원)
번호를 입력하고 Enter를 누르세요. (주문완료는 f를 누르세요.):""")
        
        # print("input_menu : ", input_menu)

        if input_menu.isdigit():
            input_menu = int(input_menu)
            # print("input_menu : ", input_menu)
            

            if (0 < input_menu <= len(menus)): #1~3 사이에서 선택
                choice_menu = menus[input_menu-1]
                print(f"선택된 메뉴:{choice_menu}")
                order.append(choice_menu)
            else:
                print("숫자를 잘못입력하셨습니다.")

        elif input_menu == 'f':
            break
    
    print(f"주문 내역 : \n {order}")

#############################################################
# def main():
#     print("빅데이터 피자 가게에 오신 것을 환영합니다.")
#     menus = ['페퍼로니 피자', '스테이크 피자', '시푸드 피자']
#     price = [29000, 32000, 32000]
#     order = []

#     while True:
#         print("\n피자를 선택하세요. 수량 추가를 위해 여러번 선택 가능합니다.")
#         for idx, item in enumerate(menus):
#             print(f"{idx+1}.{item} ({price[idx]}원)")

#         choice = input("번호를 선택하고 Enter를 누르세요.(주문완료는 f를 누르세요) : ")

#         if choice.isdigit():
#             index = int(choice) -1
#             order.append(menus[index])
#             print(f"선택된 메뉴 : {menus[index]}")
#         elif choice == 'f':
#             break
#         else:
#             print("잘못된 입력입니다. 다시 시도해주세요.")
        


step1()

if __name__ == '__step1__' :

    menus = ['페퍼로니 피자', '스테이크 피자', '시푸드 피자']
    price = [29000, 32000, 32000]
    order = []