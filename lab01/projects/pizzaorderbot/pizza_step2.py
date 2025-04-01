

def main():

    menus = {
    '피자': ['페퍼로니 피자', '스테이크 피자', '시푸드 피자'],
    '토핑': ['햄', '페퍼로니', '트러플', '올리브', '새우']
    }

    prices = {
    '피자': [29000, 32000, 32000],
    '토핑': [500, 500, 800, 300, 800]
    }

    order = {'피자': [], '토핑': []}
    categories = ['피자', '토핑'] 
    i = 0
    current_category = categories[i]
    

    ######################################

    # 피자 선택(step1) --> 토핑 선택으로 이동. ->다시 피자 선택 
    #주문 내역 : 사전 :
    while True:
        
        print(f"\n{current_category}를 선택하세요.")
        # print("menus[current_category[i] : ",menus[current_category])
        # 피자 선택
        for idex, item in enumerate(menus[current_category]):#페퍼로니,스테이크,시푸드
            #         1      페퍼로니      29000
            print(f"{idex+1}.{item} ({prices[current_category][idex]}원)")
            #숫자 입력 1 2 3

        choice = input("번호를 선택하고 Enter를 누르세요.(주문완료: f) : ")

        if choice.isdigit():
            index = int(choice)-1 # 0 1 2
            order[current_category].append(menus[current_category][index]) #order의 피자에 
            print(f"선택된 메뉴 : {menus[current_category][index]}")
        elif choice == 'f':
            break
                
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")

        i += 1
        current_category = categories[i % 2]


        


        
        
       
    
    print("\n주문 내역 : \n", order)

            
        


main()


