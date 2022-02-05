# 문자열의 인덱싱
# 문자열에는 각 문자에 해당하는 번호(인덱스)가 존재함
# 문자열[인덱스] 를 이용해 문자열에서 문자를 추출할 수 있음
# 인덱스는 0부터 시작하며, 파이썬은 음수 인덱스도 사용할 수 있음을 참고

word = "Python"
print(len(word))

print(word[0])
print(word[5])
# len(word)-1는 문자열의 가장 마지막 문자를 반환하기 위해 사용할 수 있음
print(word[len(word)-1])
# 문자열 인덱스 범위 밖의 값을 주면 index out of range라는 에러가 발생함
# print(word[100])

# 파이썬에서는 한번 작성된 문자열은 변경 불가능함
# word[2] = "B"

# 사용자로부터 3개의 문자열을 입력 받아,
# 각 문자열의 첫번째 문자만 인덱싱 하여 새로운 문자열 만드는 프로그램

firstWord = input("첫번째 문자열을 입력하세요. : ")
secondWord = input("두번째 문자열을 입력하세요. : ")
thirdWord = input("세번째 문자열을 입력하세요. : ")

finalWord = firstWord[0] + secondWord[0] + thirdWord[0]
print("새로 만든 문자열: ", finalWord)


