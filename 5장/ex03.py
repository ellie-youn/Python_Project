# 1부터 사용자가 입력한 수(num)까지의 합계를 구하는 프로그램 (for문 이용)

num = int(input("숫자를 하나 입력하세요. >>"))
sum = 0
for i in range(1, num+1):
    sum += i
print("1부터 ", num, "까지의 합은 ", sum)