# 140학점을 이수하고 평점 2.0 이상이 되어야 졸업 가능할 때,
# 사용자에게 이수학점과 평점을 입력받아 졸업가능 여부를 확인하는 프로그램

inputCredit = int(input("이수하신 학점을 입력해 주세요. >> "))
inputGPA = float(input("귀하의 평점을 입력해 주세요. >> "))

if (inputCredit >= 140) and (inputGPA >= 2.0):
    print("귀하께서는 졸업 요건을 만족하셨습니다.")
else:
    print("귀하께서는 졸업 요건을 만족하지 못하셨습니다.")

