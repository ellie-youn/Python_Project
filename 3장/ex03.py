# 자동 판매기를 시뮬레이션 하는 프로그램
# 사용자는 1,000원 지폐, 500원 및 100원 동전을 사용할 수 있음
# 물건 값을 사용자로부터 입력 받아, 지폐 및 동전 개수를 입력하면
# 거스름돈을 계산하여 동전으로 반환하는 프로그램

itemPrice = int(input("선택하신 물건은 얼마입니까?: "))
bills_1000 = int(input("천원권 지폐의 개수는 몇 개 입니까?: "))
coins_500 = int(input("오백원 동전의 개수는 몇 개 입니까?: "))
coins_100 = int(input("백원 동전의 개수는 몇 개 입니까?: "))

# 거스름돈 구하기
nodMoney = ((bills_1000 * 1000) + (coins_500 * 500) + (coins_100 * 100)) - itemPrice
print("거스름돈: ", nodMoney)

# 거스름돈(500원)
nod_500 = nodMoney // 500
nodMoney = nodMoney % 500 # 500원으로 나눈 나머지 값

# 거스름돈(100원)
nod_100 = nodMoney // 100
nodMoney = nodMoney % 100 # 100원으로 나눈 나머지 값

# 거스름돈(50원)
nod_50 = nodMoney // 50
nodMoney = nodMoney % 50 # 50원으로 나눈 나머지 값

# 거스름돈(10원)
nod_10 = nodMoney // 10
nodMoney = nodMoney % 10 # 10원으로 나눈 나머지 값

# 거스름돈(1원)
nod_1 = nodMoney

print("500원 개수: ", nod_500, "100원 개수: ", nod_100, "50원 개수: ", nod_50, "10원 개수: ", nod_10, "1원 개수: ", nod_1)

