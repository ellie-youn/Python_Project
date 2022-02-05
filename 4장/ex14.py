# 몸무게와 키를 입력받아 BMI 수치를 계산하는 프로그램
# BMI가 20.0 이상 25.0 미만이면 표준, 아니면 체중 관리가 필요함
# BMI = 몸무게 / (키(m) * 키(m)) -> cm로 키를 받아 m로 변환 필요

print("BMI를 계산하기 위해 아래 정보를 입력해 주세요.")
height = float(input("키를 입력하세요. >> "))
weight = float(input("몸무게를 입력하세요. >> "))
height /= 100.0 # 복합 대입 연산자를 사용 -> height = height / 100.0과 동일
BMI = weight / (height * height)
print(BMI)

if (BMI >= 20.0) and (BMI < 25.0):
    print("귀하의 BMI는 표준입니다.")
else:
    print("귀하께서는 체중관리가 필요합니다.")
