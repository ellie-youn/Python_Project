# 학점을 세부적으로 구분하는 프로그램(중첩 if)
# 1) 사용자로부터 점수를 입력 받음
# 2) 점수가 95 이상 100 이하면 A+
# 3) 점수가 90 이상 94 이하라면 A0
# 4) B, C, D 학점도 위와 같이 출력

userScore = int(input("귀하의 점수를 입력하세요. >> "))
userGrade = 0

if userScore >= 90:
    if userScore >= 95:
        userGrade = "A+"
    else:
        userGrade = "A0"
elif userScore >= 80:
    if userScore >= 85:
        userGrade = "B+"
    else:
        userGrade = "B0"
elif userScore >= 70:
    if userScore >= 75:
        userGrade = "C+"
    else:
        userGrade = "C0"
elif userScore >= 60:
    if userScore >= 65:
        userGrade = "D+"
    else:
        userGrade = "D0"
else:
    userGrade = "F"

print("귀하의 점수는 %s, 학점은 %s입니다." % (userScore, userGrade))
