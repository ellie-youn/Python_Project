# 사용자에게 두 개의 정수를 입력 받아 둘 중 큰 수를 출력하는 프로그램

numA = int(input("첫번째 정수를 입력하세요. >> "))
numB = int(input("두번째 정수를 입력하세요. >> "))

if numA > numB:
    print("첫번째 정수 %s 가 두번째 정수 %s 보다 큽니다." % (numA, numB))
elif numA < numB:
    print("두번째 정수 %s 가 첫번째 정수 %s 보다 큽니다." % (numB, numA))
else:
    print("입력하신 두 정수의 크기는 같습니다.")


x = int(input("첫번째 정수를 입력하세요. >> "))
y = int(input("두번째 정수를 입력하세요. >> "))
maximum = 0

if x > y:
    maximum = x
else:
    maximum = y

print("둘 중 큰 수는 ", maximum)