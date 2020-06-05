import turtle
import time
import random 

delay = 0.1

#Score
score = 0
high_score = 0
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

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))


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
window.onkeypress(go_left, "l")
window.onkeypress(go_right, "r")


# Main game loop
while True:
    window.update()

    #Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
    
    # Hide the segments
    for segment in segments:
        segment.goto(1000,1000)
    
    # Clear the segments list 
    segments.clear()

    #Reset the score
    score = 0

    #reset the delay
    delay = 0.1

    pen.clear()
    pen.write("Score: {} High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))

    # check for a collision with the food
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

        #Reduce the delay
        delay -= 0.001

        #Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))


    # move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # move the end segments 0 to where the end is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()


    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)
    
    segments.clear()

    # reset the score 
    score = 0
    
    #reset the delay
    delay = 0.1

    #Update the display score
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
   
    time.sleep(delay)
window.mainloop()