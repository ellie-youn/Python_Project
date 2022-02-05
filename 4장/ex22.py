# 사용자로부터 입력받은 달의 일수를 구하는 프로그램

input_month = int(input("원하시는 달을 입력하세요. >> "))
monthWith28 = [2]
monthWith30 = [4, 6, 9, 11]
monthWith31 = [1, 3, 5, 7, 8, 10, 12]

if input_month in monthWith31:
    print("%s월에는 총 31일이 있습니다." % input_month)
elif input_month in monthWith30:
    print("%s월에는 총 30일이 있습니다." % input_month)
else:
    print("%s월에는 총 28일이 있습니다." % input_month)

# 인프런 코드
if input_month == 2:
    print(input_month, "월의 일수는 28일")
elif (input_month == 4) or (input_month == 6) or (input_month == 9) or (input_month == 11):
    print(input_month, "월의 일수는 30일")
else:
    print(input_month, "월의 일수는 31일")