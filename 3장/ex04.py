# 문자열에 대한 실습

# 큰 따옴표(Double Quotation)
welcome = "Happy New Year 2022"
print(welcome)

# 작은 따옴표(Single Quotation)
welcome = 'Happy New Year 2022'
print(welcome)

# 문자열을 만들 때 따옴표 시작과 끝이 동일한지 반드시 확인
# welcome = "Happy New Year 2022'
# print(welcome)

message = "은혁이가 '안녕하세요'라고 인사했습니다."
print(message)

message = "doesn\'t"
print(message)

message = "\"Yes,\" I can do it!"
print(message)

# 특수문자 형태인 \n은 개행(Enter)을 하는 문자이다
message = "First\nSecond\nThird"
print(message)

# 특수문자 \t는 탭만큼 띄우는 문자이다
# 문자열 앞에 r을 입력하면 이스케이프 문자의 기능을 제거할 수 있음
message = r"C:\temp\name"
print(message)

# 문자열의 길이를 알기 위해서는 len() 함수를 이용
message = "World"
print("문자열의 길이 : ", len(message))

message = "윤혜영"
print("문자열의 길이 : ", len(message))