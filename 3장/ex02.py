# 지구에서 가장 가까운 별은 프록시마 켄타우리
# 프록시마 켄타우리는 지구로부터 40 * 10의 12승 km 떨어져 있을 때,
# 이 별까지 빛의 속도로 간다면 얼마 만큼의 시간이 걸리는지 계산하는 프로그램

from math import *
# 빛의 속도 값 저장
light_speed = 300000
distance = 40 * pow(10, 12)

# 시간 = 거리 / 속도
sec = distance / light_speed
print("소요 시간은", sec, "초")
light_year = sec / (60 * 60 * 24 * 365)
print("소요 기간은", light_year, "년")