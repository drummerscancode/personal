# Submitted as http://www.codeskulptor.org/#user13_nbWZ5tdZJS_3.py
# Implementation of classic arcade game Pong
import simplegui
import random


# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 10
HALF_BALL_RADIUS = BALL_RADIUS / 2
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
time = 0 # the time since the start of game
ball_pos, ball_vel = [0, 0] # the current pos and vel of ball
paddle1_pos, paddle2_pos = 0.0, 0.0 # these are floats according to template
paddle1_vel, paddle2_vel = 0.0, 0.0
score1, score2 = 0, 0 


def tick():
    """ Counts the 10's of seconds passed. """
    global time
    time += 1

    
# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global time, ball_pos, ball_vel
    time = 0
    ball_pos = [WIDTH/2, HEIGHT/2]
 
    if right:
        ball_vel = [random.randrange(2, 4), -random.randrange(1, 3)]    
    else:
        ball_vel = [-random.randrange(2, 4), -random.randrange(1, 3)]
        
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2
    
    score1, score2 = 0, 0
    paddle1_pos, paddle2_pos = HEIGHT/2, HEIGHT/2
    paddle1_vel, paddle2_vel = 0, 0
    ball_init(False)
    

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
 
    # update paddle's vertical position, keep paddle on the screen
    if not (paddle1_pos - HALF_PAD_HEIGHT + paddle1_vel < 0 or paddle1_pos + HALF_PAD_HEIGHT + paddle1_vel > HEIGHT):
        paddle1_pos += paddle1_vel
    if not (paddle2_pos - HALF_PAD_HEIGHT + paddle2_vel < 0 or paddle2_pos + HALF_PAD_HEIGHT + paddle2_vel > HEIGHT):
        paddle2_pos += paddle2_vel
    # draw paddles
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "Grey")
    c.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "Grey")

        
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    # check if the ball touches the ceiling or the floor
    if (ball_pos[1] < 0 + HALF_BALL_RADIUS) or (ball_pos[1] > HEIGHT - HALF_BALL_RADIUS):
        ball_vel[1] = -ball_vel[1] # change the velocity
        ball_pos[1] = ball_pos[1] + ball_vel[1]
    
   
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH: # is the ball on the left gutter?
        if ball_pos[1] < paddle1_pos - HALF_PAD_HEIGHT or ball_pos[1] > paddle1_pos + HALF_PAD_HEIGHT: 
            score2 += 1
            ball_init(True)
        else: # bounce 
            ball_vel[0] = -1.1*ball_vel[0] # increase 10%
            ball_vel[1] = 1.1*ball_vel[1]
            ball_pos[0] = ball_pos[0] + ball_vel[0]
    elif ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        if ball_pos[1] < paddle2_pos - HALF_PAD_HEIGHT or ball_pos[1] > paddle2_pos + HALF_PAD_HEIGHT: 
            score1 += 1 
            ball_init(False)
        else: # D.R.Y.
            ball_vel[0] = -1.1*ball_vel[0]
            ball_vel[1] = 1.1*ball_vel[1]
            ball_pos[0] = ball_pos[0] + ball_vel[0]
    
    
    
    
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, 'Red', 'White')
    c.draw_text(str(score1), (20, 20), 25, 'Yellow')
    c.draw_text(str(score2), (WIDTH-20, 20), 25, 'Green')
     
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -1 # constant velocity
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 1
    print chr(key)
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -1 
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 1
   
        
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button = frame.add_button('Restart', new_game)

timer = simplegui.create_timer(10, tick)
timer.start()

# start frame
frame.start()
new_game()
