# 숫자 추측 게임

from random import *
# 1~100 사이의 난수를 발생
targetNumber = randint(1, 100)
print(targetNumber)
userNumber = int(input("1에서 100 사이의 숫자를 맞춰보세요. >> "))
cnt = 0

while True:
    if targetNumber == userNumber:
        cnt += 1
        print("정답입니다. 게임을 종료합니다. (시도횟수 : ", cnt, ")")
        break
    elif targetNumber <= userNumber:
        print("입력한 숫자가 더 큽니다.")
        cnt += 1
        print("(시도횟수 : ", cnt, ")")
    else:
        print("입력한 숫자가 더 작습니다.")
        cnt += 1
        print("(시도횟수 : ", cnt, ")")
    userNumber = int(input("다시 입력해 주세요. >> "))

