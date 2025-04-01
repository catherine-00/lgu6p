h = float(input("키를 입력하세요(cm) : "))
w = float(input("몸무게를 입력하세요(kg) : "))

h = h*0.01
bmi = round(w/(h**2),3)

# if (18.5 < bmi ) :

#     if(23 < bmi):

#         if (25.00 < bmi):
#             print(bmi," : 비만")
#         else:
#             print(bmi," : 과체중")
#     else:
#         print(bmi," : 정상")

# else:
#     print(bmi, " : 저체중")


if bmi >= 25 :
    print(bmi, " : 비만")
elif bmi >= 23:
    print(bmi,"과체중")
elif bmi >= 18.5:
    print(bmi, "정상")
else :
    print(bmi,"저체중")

    



 

