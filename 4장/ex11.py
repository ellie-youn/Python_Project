# 문자열 중앙 문자를 추출하여 출력하는 프로그램
# 단, 짝수개의 문자를 가진 문자열은 가운데 2개 문자를 출력함

letters = input("문자열을 입력하세요. >> ")
length_letters = len(letters)

if length_letters % 2 == 0:
    center_character1 = letters[length_letters//2-1]
    center_character2 = letters[length_letters//2]
    print("중앙에 있는 두 문자는 %s, %s입니다" % (center_character1, center_character2))
else:
    center_character = letters[length_letters//2]
    print("중앙에 있는 문자는 %s입니다" % center_character)


