# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:14:08 2016

@author: Kevin Carter
"""

import random
import turtle
#===================Set up the screen and Turtle=================
wn=turtle.Screen()
t = turtle.Turtle()
t.pensize(5)
Scr_WIDTH, Scr_HEIGHT = 800, 800
wn.setup(Scr_WIDTH,Scr_HEIGHT)
wn.tracer(0)


bg_color = "blue"

wn.bgcolor(bg_color)


#===================Set up Globals and initial conditions================
game_over = False
score = 0

v = 3
sq_size = (Scr_WIDTH / 8 )//2 * 2            #Set a square size proportional to the screen and round it off
sq_x, sq_y = 0 , -Scr_HEIGHT/2 + sq_size   #Set square position

hole_width = (sq_size * 5/2)//2 * 2  #Set a reasonable hole width for the square to pass through


#----------------Left Blocker---------------

Lb_w, Lb_h = random.randint(0,Scr_WIDTH - hole_width), sq_size  #Generate a random width for the left blocker
Lb_x, Lb_y = -Scr_WIDTH/2 , Scr_HEIGHT/2 + Lb_h  #designate the position of left blocker

#----------------Right Blocker--------------
Rb_x , Rb_y = Lb_x + Lb_w + hole_width,  Lb_y  #Get the position of the right blocker from the left blocker
Rb_w , Rb_h = Scr_WIDTH - Lb_w + hole_width , Lb_h      #Get the height and width of the right blocker from the left blocker
   





def draw_square(t, sq_x, sq_y, sq_size, color = "#33cc33" ):
  """Draws the player square"""
  t.color(color)
  t.begin_fill()
  t.up()
  t.goto(sq_x, sq_y)
  t.setheading(0)  #Face right
  t.down()
  for side in range(4):
    t.forward(sq_size)
    t.right(90)
  t.end_fill()
  
  
def draw_Leftblocker(t,Lb_x, Lb_y, Lb_w, Lb_h,color = "#ff9900"):
  """Draws the left blocker"""
  t.color(color)
  t.begin_fill()
  t.up()
  t.goto(Lb_x, Lb_y)
  t.setheading(0)  #Face right
  t.down()
  for side in range(2):
    t.forward(Lb_w)
    t.right(90)
    t.forward(Lb_h)
    t.right(90)
  t.end_fill()

def draw_Rightblocker(t,Rb_x, Rb_y, Rb_w, Rb_h,color = "#ff9900"):
  """Draws the Right blocker"""
  t.color(color)
  t.begin_fill()
  t.up()
  t.goto(Rb_x, Rb_y)
  t.setheading(0)  #Face right
  t.down()
  for side in range(2):
    t.forward(Rb_w)
    t.right(90)
    t.forward(Rb_h)
    t.right(90)
  t.end_fill()
  
def write_score():
    """Updates the score label"""
    t.up()
    t.goto(-Scr_WIDTH/2+60 , Scr_HEIGHT/2-40)
    t.down()
    score_label = "Score: " + str(score)
    t.write(score_label , align = "center", font = ("Arial", 24 ,"bold"))

  
def handle_left():
    """Pressing left changes the global velocity variable to a negative value
    """
    global v
    print('left pressed')
    v = -4

def handle_right():
    """Pressing right changes the global velocity variable to a positive value
    """
    global v
    print('right pressed')
    v = 4



#draw_square(t, sq_x, sq_y, sq_size, color = "#7777aa" )

def next_frame():
    t.clear()
    
    #-----Make the blockers fall-----
    global sq_x, Lb_y, Rb_y , v , Lb_w , Rb_x,Rb_w, game_over, score
    Lb_y -= 3
    Rb_y -= 3
    if sq_x <= -Scr_WIDTH / 2:  #bounce off left wall
      v = 4
      sq_x += v
    elif sq_x >= Scr_WIDTH / 2 - sq_size:   #bounce off right wall
      v = -4
      sq_x += v
    else:
      sq_x += v     #Make the square move according to current velocity
    
    #-----Check for collisions if collisions are possible in the current frame---
    if Lb_y - Lb_h <= -Scr_HEIGHT / 2 + sq_size :
      if sq_x <= Lb_x + Lb_w or sq_x + sq_size >= Rb_x:
        wn.bgcolor("red")
        score_label = "Score: " + str(score)
        t.up()
        t.goto(0,0)
        t.down()
        t.color("black")
        t.write('Game Over', align = "center", font = ("Arial", 48,"bold"))
        t.up()
        t.goto(0,-50)
        t.down()
        t.write(score_label, align = "center", font = ("Arial", 36,"bold"))
        game_over = True  #End the game if collision happens

        
      
    
    #Reset and create new blockers if the blockers fall below the screen
    if Lb_y <= -Scr_HEIGHT / 2:
      Lb_y = Scr_HEIGHT/2 + Lb_h
      Lb_w = random.randint(0,Scr_WIDTH - hole_width)
      
      Rb_x , Rb_y = Lb_x + Lb_w + hole_width,  Lb_y  
      Rb_w  = Scr_WIDTH - Lb_w + hole_width
      score += 1
    
    
    draw_Leftblocker(t,Lb_x, Lb_y, Lb_w, Lb_h,color = "#ff9900")
    draw_Rightblocker(t,Rb_x, Rb_y, Rb_w, Rb_h,color = "#ff9900")
    draw_square(t, sq_x, sq_y, sq_size, color = "#33cc33" )
    write_score()
    
    if not game_over:
      wn.ontimer(next_frame, 3)
      wn.update()
    
      





wn.onkeypress(handle_left, 'Left')
wn.onkeypress(handle_right, 'Right')
t.hideturtle()


next_frame()
wn.listen()

wn.mainloop()

