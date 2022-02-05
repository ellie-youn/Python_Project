# 사용자로부터 입력받은 연도의 윤년 여부를 판단하는 프로그램
# 윤년의 조건
# 1) 연도가 4로 나누어 떨어지면 윤년
# 2) 연도가 100으로 나누어 떨어지면 윤년이 아님
# 3) 연도가 400으로 나누어 떨어지면 윤년

input_year = int(input("원하시는 연도를 입력해 주세요. >> "))

if input_year % 4 == 0:
    if input_year % 100 == 0:
        print(input_year, "는 윤년이 아닙니다.")
    elif input_year % 400 == 0:
        print(input_year, "는 윤년입니다.")
    else:
        print(input_year, "는 윤년입니다.")
else:
    print(input_year, "는 윤년이 아닙니다.")

# 인프런 코드
if (input_year % 4 == 0) and (input_year % 100 != 0) or (input_year % 400 == 0):
    print(input_year, "는 윤년입니다.")
else:
    print(input_year, "는 윤년이 아닙니다.")