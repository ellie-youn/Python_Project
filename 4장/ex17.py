# 사용자로부터 입력받은 정수를 판단하는 프로그램
# 음수, 0, 양수 중 1개 결과를 출력

number = int(input("정수를 입력해 주세요. >> "))

if number != 0:
    if number > 0:
        print("입력하신 정수는 양수입니다.")
    else:
        print("입력하신 정수는 음수입니다.")
else:
    print("입력하신 정수는 0입니다.")


if number > 0:
    print("입력하신 정수는 양수입니다.")
elif number == 0:
    print("입력하신 정수는 0입니다.")
else:
    print("입력하신 정수는 음수입니다.")