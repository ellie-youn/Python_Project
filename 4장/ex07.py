# 사용자에게 정수를 입력받아 홀수/짝수를 말해주는 프로그램

number = int(input("정수를 입력해 주세요. >> "))

if number % 2 == 0:
    print("귀하께서 입력하는 숫자는 짝수입니다.")
else:
    print("귀하께서 입력하신 숫자는 홀수입니다")