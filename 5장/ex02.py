# range() 함수 실습

# 1) range(x) : 매개변수 1개
hap = 0
for x in range(10):
    hap = hap + x
print("0 ~ 9까지의 합:", hap)

# 2) range(x, y) : 매개변수 2개 / x부터 y-1까지 정수
hap = 0
for x in range(0, 10):
    hap = hap + x
print("0 ~ 9까지의 합:", hap)

# 3) range(x, y, z) : 매개변수 3개 / x부터 y-1까지, z간격의 정수
hap = 0
for x in range(0, 10, 1):
    hap = hap + x
print("0 ~ 9까지의 합:", hap)

# 문자열 실습
# 문자열은 시퀀스 대상이므로 for 문을 통해 문자를 추출/출력할 수 있음

s = "Katharina my name"
for cha in s:
    print(cha, end=" ")
