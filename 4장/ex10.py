# 5만원 이상 구입 시 5% 할인을 해주는 쇼핑몰
# 사용자에게 구입 금액을 입력 받은 후 할인 금액 및 지불 금액을 출력하는 프로그램

purchaseAmount = int(input("구매하신 금액을 입력하세요. >> "))
discountRate = 0.05
discountAmount = 0
finalAmount = 0

if purchaseAmount >= 50000:
    finalAmount = purchaseAmount * (1-discountRate) # 지불금액
    discountAmount = purchaseAmount * discountRate # 할인 금액
else:
    finalAmount = purchaseAmount

print("구입금액은 %s 원 입니다." % purchaseAmount)
print("할인금액은 %s 원 입니다." % discountAmount)
print("지불금액은 %s 원 입니다. " % finalAmount)
