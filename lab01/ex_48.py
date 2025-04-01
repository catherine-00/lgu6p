#file 열기
#ex_48.py가 있는 폴더에 file_w.txt가 생성되는 것.

# with open("file_w.txt",'r',encoding='utf-8') as f:
#     lines = f.readlines()
#     print(lines, type(lines))
#     for line in lines:
#         print(line,end='')

import os, ex_45

data = os.listdir('./data')
# print("data 폴더 안 파일 : ", data)
for d in data:
    # print("for문 안의 d: ",d)
    d_s = d.split('.')
    # print("d_s: ",d_s)
    if d_s[-1] == 'xlsx' :
        data.remove(d)
print("data:",data,'\n') # data = ['jisoo.txt', 'mansoo.txt']

#code폴더의 data폴더에 지수와 만수의 txt를 불러와서 내용 읽기

for file in data: # file = 지수.txt
    l=[]
    print("\n","현재 읽고 있는 file : ", file,'\n')

    with open(f"./data/{file}",'r',encoding='utf-8') as f: #지수txt읽기
        lines = f.readlines()
        for line in lines:
            line = float(line) #string을 float로 바꿔서 저장하기
            # print(line)
            l.append(line)
               
        print("l : ", l,'\n')
    m = ex_45.mean(l)
    s = ex_45.std(l)

    print(f"이름 : {file[:-4]} : 평균 : {m:.2f}, 표준편차 : {s:.2f}")

    with open("score.txt",'a',encoding='utf-8') as f:
        f.write(f"이름 : {file[:-4]} : 평균 : {m:.2f}, 표준편차 : {s:.2f} \n")









        
        


    









# ex_45.mean(), ex_45.std()


