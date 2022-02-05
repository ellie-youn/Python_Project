# 부울(Bool) 변수 알아보기
# 부울 변수는 플래그 변수 형태로 사용하는 경우가 많음

flag = True
print(type(flag))
print(flag)

flag = not flag
print(type(flag))
print(flag)

if flag:
    print("참이므로 실행됩니다")
else:
    print("거짓이므로 실행됩니다")
    flag = not flag

if flag:
    print("참이므로 실행됩니다")
else:
    print("거짓이므로 실행됩니다")


