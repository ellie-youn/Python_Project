# 1~100까지 누적값을 구하는 중, 누적값이 2000이상이면 for 문을 빠져나오는 프로그램

hap = 0

for i in range(1,101):
    if hap >= 2000:
        print("마지막으로 더해지는 i의 값: ", i-1)
        break
    else:
        hap += i

print("누적값: ", hap)