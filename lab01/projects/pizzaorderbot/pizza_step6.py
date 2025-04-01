import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')




def main():

    menus = {
    '피자': ['페퍼로니피자', '스테이크피자', '시푸드피자'],
    '토핑': ['햄', '페퍼로니', '트러플', '올리브', '새우'],
    '사이드': ['치즈오븐스파게티', '리조또', '치킨윙'],
    '음료': ['콜라', '스프라이트', '오렌지쥬스']
    }
    prices =    {
 '피자': [29000, 32000, 32000],
 '토핑': [500, 500, 800, 300, 800],
 '사이드': [9900, 8900, 8900],
 '음료': [1000, 1000, 1000]
 }


    order = {'피자': [], '토핑': [], '사이드' : [], '음료' : []}
    categories = ['피자', '토핑','사이드','음료'] 
    i = 0
    total_price = 0
    err_msg =""
    

    ######################################

    # 피자 선택(step1) --> 토핑 선택으로 이동. ->다시 피자 선택 
    #주문 내역 : 사전 :
    while True:
        clear_screen()
        if err_msg != "":
            print(err_msg)
            err_msg=""



        current_category = categories[i]
        
        print(f'\n=========================\n{current_category}를 선택하세요.')
        print(f"\n현재 장바구니 : {order}\n")
        # print("menus[current_category[i] : ",menus[current_category])
        # 피자 선택
        for idex, item in enumerate(menus[current_category]):#페퍼로니,스테이크,시푸드
            #         1      페퍼로니      29000
            print(f"{idex+1}.{item} ({prices[current_category][idex]}원)")
            #숫자 입력 1 2 3

        choice = input("\n번호를 선택하고 Enter를 누르세요.(다음단계 : n, 이전단계 : p, 주문완료: f) : ")
      

        if choice.isdigit():
            index = int(choice)-1 # 0 1 2
            if (0 <= index < len(menus[current_category])):
                order[current_category].append(menus[current_category][index]) #추가
                total_price += prices[current_category][index] #가격계산
                print(f"선택된 메뉴 : {menus[current_category][index]}")
            else :
                err_msg = "[!] 잘못된 선택입니다. 다시 선택하세요."
                # print("\n[!]잘못된 선택입니다. 다시 선택하세요.")

        elif choice == 'f':
            break
        elif choice == ('n'):
            i += 1      

            # print("i:" ,i)
        elif choice == ('p'):
            i -= 1
            
            # print("i : ", i)
        else:
            err_msg = "[!] 잘못된 선택입니다. 다시 선택하세요."
            # print("\n [!]잘못된 선택입니다. 다시 선택하세요.")
        
        
            
    print("""
---------
주문 내역
---------
              """)
    
    for k,v in order.items():
        
        print(f"{k} : {','.join(v)}")
    print(f"총 금액 : {total_price} 원")
    print("주문이 완료되었습니다. 감사합니다.")

    
       


main()