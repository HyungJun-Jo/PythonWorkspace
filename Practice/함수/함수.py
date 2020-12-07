
# method 정의
def open_account():
    print("새로운 계좌가 생성되었습니다.")

# method 인자값 전달
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

# method 사용
balance = 0  # 잔액
open_account()
balance = deposit(balance, 1000)
print(balance)


# 가변인자
def profile(name, age, *language):
    print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")

profile("유재석", 20, "Python", "Java")