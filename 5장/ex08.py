# 사용자로부터 입력을 받아, 구구단을 출력하는 프로그램

number = int(input("2에서 9사이의 숫자를 입력하세요. >> "))

for num in range(1, 10):
    if number < 2 or number >9:
        print("숫자를 잘못 입력하셨습니다.")
        break
    else:
        print(number, "X", num, "=", number * num)