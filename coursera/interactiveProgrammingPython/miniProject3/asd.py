# template for "Stopwatch: The Game"
# Submitted: http://www.codeskulptor.org/#user12_KdvMFCyU0cHjTqE_0.py

import simplegui

stopwatch = 0 # the time, suggested to use ints instead of floats
height = 400 # for the frame
width = 400
timer = '' # the timer object
stop_counter = 0 # counter of stops
whole_counter = 0 # counter of whole second stops


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t): # t is in tenths of seconds
    return '%d:%02d.%d' % (t//600, (t%600)//10, t%10)    
    
    
def start_handler():
    timer.start()	

    
def stop_handler():
    if timer.is_running():
        global stop_counter, whole_counter
        stop_counter += 1
        if format(stopwatch).partition('.')[2] == '0': # split is not supported in Codeskulptor?
            whole_counter += 1
        
        timer.stop()

        
def reset_handler():
    global stopwatch, stop_counter, whole_counter
    
    stop_handler()
    stopwatch = 0
    stop_counter = 0
    whole_counter = 0
    

def timer_handler():
    global stopwatch
    stopwatch += 1 # in tenths of seconds
    
    
def draw_handler(canvas):
    canvas.draw_text(format(stopwatch), (width/2, height/2), 20, "Green")
    canvas.draw_text('%d/%d' %(whole_counter, stop_counter), (width-50, 20), 20, "Green")
    

frame = simplegui.create_frame("Stopwatch game", width, height)
frame.add_button("Start", start_handler, 50)
frame.add_button("Stop", stop_handler, 50)
frame.add_button("Reset", reset_handler, 50)
timer = simplegui.create_timer(100, timer_handler) # 100ms = 0.1s
frame.set_draw_handler(draw_handler)

frame.start()
