# 내장 함수 및 math 라이브러리 이용

# 한번만 호출해도 됨. math 라이브러리의 모든 합수를 사용할 수 있음
from math import *

# 절대값 구하기
print(abs(-77))
print(abs(77))

# 반올림하기
print(round(1.2222))
print(round(1.522))

# 주어진 매개변수 값 중에서 최대값 구하기
print(max(10, -20, 100, 9999))
# 주어진 매개변수 값 중에서 최소값 구하기
print(min(10, -20, 100, 9999))

# 4.0의 제곱근 구하기
print(sqrt(4.0))

# 제곱 구하기(3의 2승), 연산자 **와 동일함
print(pow(3, 2))
