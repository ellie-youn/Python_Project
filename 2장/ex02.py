# 사용자로부터 참석하는 인원의 수를 받아, 해당하는 인원 수에 따라
# 치킨은 인원당 1마리, 맥주는 인원당 2병, 케이크는 인원당 4조각를 배분하는 프로그램

# input() 함수는 사용자로부터 값을 입력 받아 문자열 형태로 저장함
# 문자열을 숫자 형태로 바꾸기 위하여 int() 함수를 사용함
number = int(input("참석자 수를 입력하세요 : "))

chickens = number
beers = number * 2
cakes = number * 4
print("치킨의 수 : ", chickens)
print("맥주의 수 : ", beers)
print("케이크의 수 : ", cakes)
