# 주사위 눈을 랜덤으로 발생시켜 출력하는 프로그램
# randint() 함수를 검색하여 사용법을 익힌 후 프로그램을 작성하시오

from random import *
num = randint(1, 6)
print("주사위의 눈은 %s입니다." % num)

if num == 1:
    print("주사위의 눈은 1입니다.")
elif num == 2:
    print("주사위의 눈은 2입니다.")
elif num == 3:
    print("주사위의 눈은 3입니다.")
elif num == 4:
    print("주사위의 눈은 4입니다.")
elif num == 5:
    print("주사위의 눈은 5입니다.")
else:
    print("주사위의 눈은 6입니다.")