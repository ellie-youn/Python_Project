# 문자열의 연결
# + 연산자는 문자열 사이에 들어가면 문자열을 연결해주는 역할을 한다

first_name = " Eun Hyuk"
last_name = "Shin"
name = last_name + first_name
print(name)

# 파이썬에서는 모든 데이터에 데이터 타입이 존재함
# 아래 소스코드에서 "Person"은 문자열, 100은 int 타입이므로 타입이 불일치함. 따라서 오류 발생
# 이를 해결하기 위해서는 str() 함수를 이용하여 100을 문자열로 변경/타입을 일치 시켜야 함
temp = "Person" + str(100)
print(temp)

temp = "Person" + str(100.188)
print(temp)

# 문자열을 숫자로 변환
# 정수는 int() 함수, 실수는 float() 함수를 사용
price = int("123456")
print(type(price))

price = float("123456")
print(type(price))

# 문자열의 반복
# 문자열에서 * 연산자를 사용하면 그만큼 반복이 된다
arrow = "->" * 10
print(arrow)

arrow = "->"
print(arrow * 10)

# %s(형식 지정자)
# %s는 문자열이나 숫자값을 변수에 대입하여 자주 변경이 있을 경우
# 상황에 맞게끔 출력할 수 있도록 하면 됨

# 정수대입
price = 1000
print("가격 : %s" % price)

# 문자열 대입
time = "13:49"
print("현재 시간 : %s" % time)

temp = "현재 시간은 %s 시 %s 분 %s 초입니다."
print(temp % (4, 15, 12))