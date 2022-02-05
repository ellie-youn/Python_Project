# 리스트에 대한 실습
# 리스트란, 여러 개의 값을 모아 하나의 변수에 저장한 것, 대괄호 안에 값을 저장

city = ["서울", "부산", "대구", "광주", "인천"]

# 리스트의 길이를 확인할 때도 len() 함수 사용
print(len(city))
print(city)

# 리스트에서는 해당하는 인덱스 값을 변경 가능함
city[1] = "Busan"
print(city)

# 리스트는 데이터 타입에 관계 없는 여러 개의 값을 저장할 수 있음
temp = ["대구", "부산", 100, 10.798]
print(temp)

# 한 사람의 정보를 출력
name = input("이름을 입력하세요 >> ")
age = int(input("나이를 입력하세요 >> "))
address = input("주소를 입력하세요 >> ")
height = int(input("키를 입력하세요 >> "))
weight = int(input("몸무게를 입력하세요 >> "))

person = [name, age, address, height, weight]
print(person)