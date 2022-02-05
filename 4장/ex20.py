# 중첩(nested) if ~ else 구문
# 사용자로부터 ID를 입력받아 등록 여부를 검사하는 프로그램
# 등록된 ID를 리스트 구조로 저장
# ID가 등록되어 있다면 패스워드를 물어봄 ( 단, 패스워드는 "1234"로 가정)

# 아이디 값을 리스트에 저장
idList = ["abcd", "ellie"]
# 패스워드 정의
password = "1234"

userId = input("ID를 입력하세요. >> ")

if userId in idList:
    userPassword = input("비밀번호를 입력하세요. >> ")
    if userPassword == password:
        print("로그인되었습니다.")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("등록되지 않은 ID입니다.")