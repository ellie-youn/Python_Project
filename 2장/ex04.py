# 5,000원을 가진 한 사람이 120원짜리 사탕을 구매할 때
# 최대로 구매할 수 있는 사탕의 개수를 구하는 프로그램

mymoney = 5000
candyPrice = 120

# 최대로 구매 가능한 사탕의 개수
numCandies = mymoney // candyPrice
print("최대로 살 수 있는 사탕의 개수 : ", numCandies)

# 최대 구매 가능한 사탕을 구매 후 남은 돈
change = mymoney - numCandies * candyPrice
print("최대 구매 가능한 사탕 구매 후 잔돈 : ", change)
