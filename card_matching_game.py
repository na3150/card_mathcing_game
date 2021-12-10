import tkinter
import turtle as t
import random
import time
from tkinter import *

#게임이 시작하기 전에 게임 룰을 설명해주는 것도 좋을 듯

def find_card(x, y): #클릭한 카드 찾기
    min_idx = 0
    min_dis = 100
    for i in range(16):
        distance = turtles[i].distance(x, y)
        if distance < min_dis:
            min_dis = distance
            min_idx = i
    return min_idx

def score_updata(m):
    score_pen.clear()
    score_pen.write(f"{m}  {score}점/{attempt}번 시도", False, "center", ("", 15))

def result(m):
    t.goto(0, -60)
    t.write(m, False, "center", ("", 30, "bold"))


def show_scoreboard():
    player_list.sort()


def play(x, y):
    global click_num #전역변수 사옹
    global first_pick
    global second_pick
    global attempt
    global score
    if attempt == 12:
        result("Game Over") #게임 종료
        check_more_game()
    else:
        click_num += 1
        #클릭한 이미지 찾기
        card_idx = find_card(x, y)
        turtles[card_idx].shape(img_list[card_idx])

        if click_num == 1: #첫번째 선택
            first_pick = card_idx
        elif click_num == 2:
            second_pick = card_idx
            click_num = 0 #반복되도록 0으로 초기화
            attempt += 1

            if img_list[first_pick] == img_list[second_pick]:
                score+= 1
                #정답
                score_updata("정답")
                if score == 8:
                    result("성공")
                    player_list.append((attempt, nickname))
                    print((attempt, ": ", nickname))
                    #show_scoreboard()
                    check_more_game()
            else:
                score_updata("오답")
                turtles[first_pick].shape(default_img)
                turtles[second_pick].shape(default_img)

def check_more_game():
    # 게임 한번 더 진행할 것인지 질문
    root = Tk()
    def btn_yes():
        # 게임 한번 더 진행
        root.destroy()
        t.reset()
        start_game()
    def btn_no():
        label = Label(root, text="게임이 종료되었습니다", width=300)
        label.pack()
    root.geometry("400x100")
    root.title("게임을 한번 더 진행하시겠습니까?")
    frame = tkinter.Frame(root)
    frame.pack()
    btn_yes = tkinter.Button(frame, text="예", command=btn_yes)
    btn_no = tkinter.Button(frame, text="아니오", command=btn_no)
    btn_yes.pack()
    btn_no.pack()
    root.mainloop()

def get_nickname():
    def button_click():
        global nickname
        nickname = tx_nickname.get()
        print("닉네임: " + nickname)
        window.destroy()
        start_game()
    window = Tk()  # tkinter 생성
    window.geometry("250x50")
    window.title("닉네임 입력")
    frame = tkinter.Frame(window)
    frame.pack()
    tx_nickname = tkinter.Entry(frame, width=30, bg='light pink')
    tx_nickname.pack()
    button = tkinter.Button(frame, text="입력완료", command=button_click)
    button.pack()
    window.mainloop()

def start_game():
    global turtles
    global img_list
    global score
    global click_num
    global attempt
    global first_pick
    global second_pick

    # turtle 객체 생성
    t.bgcolor("white")
    t.setup(700, 700)
    t.up()
    t.ht()
    t.goto(0, 280)
    t.write("🕹 카드 매칭 게임 🕹", False, "center", ("", 30, "bold"))

    turtles = []
    img_list = []

    score_pen = t.Turtle()
    score_pen.up()
    score_pen.ht()
    score_pen.goto(0, 230)

    click_num = 0  # 클릭 횟수 (매 2회 클릭마다 정답 체크)
    score = 0  # 점수
    attempt = 0  # 시도한 횟수
    first_pick = ""  # 첫 번째 클릭한 이미지
    second_pick = ""  # 두 번째 클릭한 이미지

    score_updata("시작")

    for x in range(4):
        for y in range(4):
            new_turtle = t.Turtle()
            new_turtle.up()
            new_turtle.speed(0)
            new_turtle.color("white")  # 배경색과 동일한 하얀색으로
            new_turtle.goto(pos_x[x], pos_y[y])
            turtles.append(new_turtle)
    t.addshape(default_img)  # 배경 설정

    for i in range(8):
        img = f"images/img{i}.gif"
        t.addshape(img)
        img_list.append(img)
        img_list.append(img)  # 같은 사진이 2번 들어가도록

    random.shuffle(img_list)  # 랜덤으로 이미지 섞기
    for i in range(16):
        turtles[i].shape(img_list[i])
    time.sleep(3)
    for i in range(16):  # 3초 후 default 이미지로 변경
        turtles[i].shape(default_img)
    t.onscreenclick(play) #게임 시작
    t.done()  # 그래픽 창이 자동으로 닫히지 않도록


default_img = "images/default_img.gif"
nickname = "" #player nickname
player_list = [] #튜플(시도 횟수, 닉네임) 형태로 저장

pos_x = [-210, -70, 70, 210]
pos_y = [-250, -110, 30, 170]

'''

'''

turtles = []
img_list = []

#점수 펜 객체 생성
score_pen = t.Turtle()
score_pen.up()
score_pen.ht()
score_pen.goto(0, 230)

#turtle 객체 생성
t.bgcolor("white")
t.setup(700, 700)
t.up()
t.ht()
t.goto(0, 280)
t.write("🕹 카드 매칭 게임 🕹", False, "center", ("", 30, "bold"))

click_num = 0 #클릭 횟수 (매 2회 클릭마다 정답 체크)
score = 0 #점수
attempt = 0 #시도한 횟수
first_pick = "" #첫 번째 클릭한 이미지
second_pick = "" #두 번째 클릭한 이미지

#닉네임 입력받기
get_nickname()

