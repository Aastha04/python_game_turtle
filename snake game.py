import turtle
import time
import random 

delay = 0.1
# set up the screen
window = turtle.Screen()
window.title("Snake and Ball")
window.bgcolor("black")
window.setup(width=500, height=600)
window.tracer(0) # Turn off the screen update


# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,80)

segments = []


# snake movement
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"

def move():
    if ( head.direction == "up"):
        y = head.ycor()
        head.sety(y + 15)
    
    if ( head.direction == "down"):
            y = head.ycor()
            head.sety(y - 15)
    
    if ( head.direction == "left"):
            x = head.xcor()
            head.sety(x - 15)
    
    if ( head.direction == "right"):
            x = head.xcor()
            head.sety(x + 15)

# Keyboard bindings
window.listen()
window.onkeypress(go_up, "u")
window.onkeypress(go_down, "d")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "s")


# Main game loop
while True:
    window.update()
 
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        food.goto(x,y)

        # Add a segment
        newsegment = turtle.Turtle()
        newsegment.speed(0)
        newsegment.shape("circle")
        newsegment.color("light green")
        newsegment.penup()
        segments.append(newsegment)
    
    move()

    time.sleep(delay)