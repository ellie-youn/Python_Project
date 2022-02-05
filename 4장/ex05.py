# 사용자에게 명령어를 입력받아 터틀그래픽을 제어하는 프로그램

import turtle
# 펜의 기능을 t라는 변수에 저장
t = turtle.Pen()
# 반복문을 무한루프하여 if 구문으로 방향을 제어하는 코드
# 무한루프 코드를 작성했다면 반드시 루프를 탈출하는 코드가 있어야 함
while True:
    direction = input("왼쪽은 LEFT, 오른쪽은 RIGHT, 종료는 QUIT를 입력하세요. >> ")
    # break는 무한루프를 탈출하는 코드임
    if direction == "QUIT":
        print("종료되었습니다.")
        break

    if direction == "LEFT":
        print("LEFT를 입력하셨습니다")
        t.left(60)
        t.forward(50)
    if direction == "RIGHT":
        print("RIGHT를 입력하셨습니다")
        t.right(60)
        t.forward(50)

# 터틀 그래픽 창을 클릭하면 창을 종료하는 코드
turtle.exitonclick()