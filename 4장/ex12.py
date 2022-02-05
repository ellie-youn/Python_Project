# 논리 연산자(Locical Operator)
# 논리 연산자의 종류: AND(논리곱), OR(논리합), NOT(논리부정)

# AND 논리 연산자 실습
name = "Rita"
age = 14
height = 160

if (age >= 14) and (height >= 160):
    print("놀이 기구를 탑승하실 수 있습니다.")
else:
    print("놀이 기구를 탑승하실 수 없습니다.")

print("-" * 40)

# OR 논리 연산자 실습
if (age >= 14) or (height >= 160):
    print("놀이 기구를 탑승하실 수 있습니다.")
else:
    print("놀이 기구를 탑승하실 수 없습니다.")

print("-" * 40)

# NOT 논리 연산자 실습
if not(1==1):
    print("입력하신 값은 참입니다.")
else:
    print("입력하신 값은 거짓입니다.")
