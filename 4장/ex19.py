# 사용자로부터 태어난 연도를 입력받아
# 초등학생, 중학생, 고등학생, 대학생, 일반인으로 분류하는 프로그램
# 분류: 8~13(초등학생), 14~16(중학생), 17~19(고등학생), 20~27(대학생), 그 외(일반인)

birthYear = int(input("출생연도를 입력하세요. >> "))
nowYear = 2022
koreanAge = nowYear - birthYear + 1

print("현재나이는 %s세 입니다." % koreanAge)

# 다중 조건문
if (koreanAge >= 8) and (koreanAge <= 13):
    print("초등학생입니다.")
elif (koreanAge >= 14) and (koreanAge <= 16):
    print("중학생입니다.")
elif (koreanAge >= 17) and (koreanAge <= 19):
    print("고등학생입니다.")
elif (koreanAge >= 20) and (koreanAge <= 27):
    print("대학생입니다.")
else:
    print("일반인입니다.")

# if koreanAge >= 28:
#     print("귀하께서는 일반인입니다.")
# elif koreanAge >= 20:
#     print("귀하께서는 대학생입니다.")
# elif koreanAge >= 17:
#     print("귀하께서는 고등학생입니다.")
# elif koreanAge >= 14:
#     print("귀하께서는 중학생입니다.")
# elif koreanAge >= 8:
#     print("귀하께서는 초등학생입니다.")
# else:
#     print("귀하께서는 일반인입니다.")