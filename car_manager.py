from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.make_car()
        self.move_speed = STARTING_MOVE_DISTANCE
                
    def make_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(x=320, y=random.randint(-250,250))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            new_x = car.xcor() - self.move_speed
            current_y = car.ycor()
            car.goto(x=new_x, y=current_y)
            
            # Removes car from array
            if car.xcor() < -320:
                self.cars.remove(car)
    
    def check_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 25:
                return True
        return False
    
    
    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT