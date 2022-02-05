# for문을 이용하여 팩토리얼(factorial)을 계산하는 프로그램
# 팩토리얼 n! 은 1부터 n까지 정수를 모두 곱한 값

factorial = 1
n = int(input("숫자를 입력하세요. >>"))

for i in range(1, n+1):
    factorial *= i

print(n, "팩토리얼 값은", factorial)