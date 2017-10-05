import turtle as t
import random

t.speed(0)                                              #거북이는 최고속도입니다
t.bgcolor("black")                                      #배경색깔 검은색입니다

t.up()                                                  #그림이 중앙에 생겨서 전체적으로 보이게 하려고 시작을 왼쪽위로 수정했습니다
t.back(300)
t.lt(90)
t.fd(175)
t.rt(90)
t.down()

n=50                                                    #반지름의 값을 유동적으로 적용시킬 수 있도록 n으로 잡았습니다

def pick_color():                                       #pick_color를 정의합니다
    colors = ["magenta","cyan","yellow","aliceblue"]    #magenta,cyan,yellow,aliceblue 중에 하나가 colors로 저장됩니다
    random.shuffle(colors)                              #랜덤으로 색깔을 섞습니다
    return colors[0]                                    #나온색깔을 결과로 돌려줍니다

for x in range(1,4):                                    #step3을 3번 반복합니다
    
    for x in range(1,4):                                #step2을 3번 반복합니다

        for x in range(1,5):                            #step1. step1을 4번 반복합니다
            random_color = pick_color()                 #pick_color를 random_color에 저장합니다
            t.fillcolor(random_color)                   #rancom_color로 색을 채웁니다
            t.begin_fill()                              #첫번째 도형의 색을 채우기 시작합니다
            t.circle(n, 180)                            #반지름이 n인 반원을 그립니다
            t.lt(90)                                    #방향을 왼쪽으로 90도 돌립니다
            t.fd(2*n)                                   #앞으로 2*n만큼 이동합니다
            t.lt(90)                                    #방향을 왼쪽으로 90도 돌립니다
            t.end_fill()                                #첫번째 도형의 색을 채웠습니다
            t.up()                                      #펜을 올립니다
            t.fd(2*n)                                   #앞으로 2*n만큼 이동합니다
            t.down()                                    #펜을 내립니다
            random_color = pick_color()
            t.fillcolor(random_color)
            t.begin_fill()                              #두번째 도형의 색을 채우기 시작합니다
            t.circle(n, -180)                           #반지름이 n인 반원을 반대로 그립니다
            t.lt(90)
            t.fd(2*n)
            t.back(2*n)
            t.end_fill()                                #두번째 도형의 색을 채웠습니다

        t.up()                                          #step2.
        t.fd(4*n)                                       #앞으로 4*n만큼 이동하여 도형이 겹치치 않게 합니다
        t.down()
        
    t.up()                                              #step3.
    t.back(12*n)                                        #뒤로 12*n만큼 이동합니다.
    t.rt(90)
    t.fd(4*n)                                           #그려진 도형밑으로 겹치치 않게 4*n만큼 앞으로 이동합니다
    t.lt(90)
    t.down()
