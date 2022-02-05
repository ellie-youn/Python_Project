# 반복문(iteration)에 대한 실습
# "안녕하세요." 5번 출력하기

for i in range(0, 5):
    print("안녕하세요.")

print("-" * 20)

# 정수 리스트를 시퀀스로 만들어 반복 횟수가 커지면 사용이 번거로움
for x in [0, 1, 2, 3, 4]:
    print("안녕하세요.")

print("-" * 20)
# range(x)를 이용하면 정수 리스트를 사용하는 것보다 효율적이고 가독성이 좋음
# range(x)는 0부터 (x-1)까지 정수 리스트를 반환
for x in range(5):
    print("안녕하세요.")

# range()함수의 타입은 range 객체 타입
print(type(range(5)))

print("-" * 20)

# 문자열 리스트를 시퀀스로 가질 때 for문
s = ["피터", "베드로", "마리아", "애쉬"]
for name in s:
    print("반갑습니다. " + name + "님!")

print("-" * 20)

# 줄바꿈을 하지 않는 end 인자값
for x in [0, 1, 2, 3, 4]:
    print(x, end="\t")
