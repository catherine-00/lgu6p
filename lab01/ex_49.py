
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        print(f"{owner}님의 계좌가 개설되었습니다. 개설 잔액은 {balance}입니다.")


    def deposit(self, amount):
        
        if amount > 0 :
            self.balance += amount
            print(f"{amount}원이 입금되었습니다.")
        else :
            print("0보다 큰 금액을 입금해주세요.")
        
    def withdraw(self,amount):
        if 0 <amount <= self.balance :
            self.balance -= amount
            print(f"{amount}원이 출금되었습니다.")
            self.get_balance()
        else:
            print("잔액 부족")


    def get_balance(self):
        print(f"계좌의 현재 잔액은 {self.balance}원 입니다.")
    
    def remittance(self, amount, account):
        print(f"{account.owner}님의 계좌로 {amount}원 송금합니다.")
        account1.withdraw(amount)
        account2.deposit(amount)


    
        

# 계좌생성
account1 = BankAccount("홍길동", 10000)
account2 = BankAccount("김철수",10000)

#계좌 송금
account1.remittance(5000, account2)
