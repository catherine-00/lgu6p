#변수,함수 이름은 보통 소문자와 언더바로 만드는 게 일반적.
#클래스는 첫 문자를 대문자로 쓰는 것이 일반적.


class Person: #사람에 대한 정보를 받으 ㄴ뒤 행동을 계산하는 함수들의 묶음.
    def __init__(self, name, height, weight): #객체 지향 중 속성
        #인자들을 받아서 변수로 지정하는 함수
        #__init__는 이름을 바꾸면 안된다.<문법>
        #괄호 안에 첫 글자는 무조건 self이다. <문법>
        #뒤에는 변수들이 온다.
        self.name = name
        self.height = height
        self.weight = weight
        #self.변수를 해줘야 함수가 끝난 뒤에도 변수 값이 사라지지 않는다.

    def speed(self): # 객체 지향 중 메서드
        # 지정한 변수들로 계산을 하는 함수
        #self만 있음 = 다른 인자 없음.
        self.print() #아래의 print() 함수를 호출한다.
        return (self.height / self.weight) * 5
    
    def print(self):
        print(f"나는 {self.name}이고 키는 {self.height}, 몸무게는 {self.weight}")


p1 = Person("Tom", 170, 100) # def __init__()가 자동 호출됨.
#p1이라는 변수 안에 name, height, weight이라는 변수가 있는 것.
# print(type(p1))

# print(p1.name, p1.height, p1.weight)

p1.print()

p2 = Person("Kim", 180, 85)
print(p2.name, p2.height, p2.weight)
p2.print()

print(p1.speed())
print(p2.speed())




