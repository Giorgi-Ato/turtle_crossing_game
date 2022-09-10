import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move, 'Up')

score = Scoreboard()

game_is_on = True
car_list = []
cnt = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cnt += 1
    if cnt == 5:
        new_car = CarManager()
        car_list.append(new_car)
        cnt = 0

    for i in car_list:
        i.move()

    for i in car_list:
        if i.xcor() < -350:
            car_list.remove(i)

    for i in car_list:
        if player.distance(i) < 25:
            score.game_over()
            game_is_on = False

    if player.ycor() > FINISH_LINE_Y:
        CarManager.speed_increase()
        score.add_score()
        player.go_to_start_pozition()

screen.exitonclick()
