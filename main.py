import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Player and its listening functions
player = Player()
screen.onkey(fun=player.move, key="Up")

car_manager = CarManager()
scoreboard = Scoreboard()

while_count = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.move_cars()

    # When player finishes, restart player
    if player.ycor() > 280:
        player.restart_player()
        car_manager.increase_speed()
        scoreboard.level += 1
        scoreboard.update_score()
        
    
    if car_manager.check_collision(player):
        game_is_on = False
        scoreboard.game_over()
    
    if while_count % 6 == 0:
        car_manager.make_car()

    while_count += 1


screen.exitonclick()