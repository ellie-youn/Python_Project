from math import *
# 파이썬에서의 자료형(Data-type)
# int형을 출력
print(type(17))
# float형을 출력
print(type(10.666))
# str형을 출력
print(type("안녕하세요"))

# 반지름이 r인 구의 부피는 4/3 * PI * r^3
# 반지름이 5인 구의 부피를 계산하는 프로그램
r = 5.0
volume = 4.0 / 3.0 * pi * pow(r, 3)
print("구의 부피는", volume)

# 구의 겉넓이는 4 * PI * r^2
# 반지름이 5인 구의 겉넓이를 계산하는 프로그램
outer_area = 4 * pi * pow(r, 2)
print("구의 겉넓이는", outer_area)