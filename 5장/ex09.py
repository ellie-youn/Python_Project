# 사용자로부터 2개의 정수를 입력 받음
# 첫번째 정수 ~ 두번째 정수 범위에서 3의 배수이며 4의 배수를 제외하고 출력

number1 = int(input("첫번째 정수를 입력하세요. >> "))
number2 = int(input("두번째 정수를 입력하세요. >> "))

for i in range(number1, number2+1):
    if (i % 3 == 0) or (i % 4 ==0):
        continue
    else:
        print(i)

