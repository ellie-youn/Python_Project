# if ~ elif ~ else(옵션)에 대한 실습

score = int(input("귀하의 성적을 입력하세요(0~100점) >> "))

if score >= 90:
    print("학점은 A입니다.")
elif score >= 80:
    print("학점은 B입니다.")
elif score >= 70:
    print("학점은 C입니다.")
elif score >= 60:
    print("학점은 D입니다.")
else:   # else 구문은 옵션이며, 다중 조건 설정 시 조건 입력하지 않음
    print("학점은 F입니다.")