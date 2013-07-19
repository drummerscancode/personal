# http://www.codeskulptor.org/#user16_A3lMvPytgt8D1iP.py
# Spaceship game
# 
import simplegui
import math
import random

WIDTH = 800 # canvas size
HEIGHT = 600
score = 0
lives = 3
time = 0.5
FRICTION_PARAM = 0.03 # reduces the velocity
SHIP_ACCEL_PARAM = 0.4 # multiplier of the forward vector
MISSILE_ACCEL_PARAM = SHIP_ACCEL_PARAM + 0.2 # should be bigger 
    # for the missile to be faster than the ship
SHIP_ANGLE_VEL = 0.1 # when the left or right key is pressed
MISSILE_LFSP = 1


class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated
    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")
# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")
# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")
# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")
# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, lifespan = MISSILE_LFSP) # was 50
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")
# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")


def angle_to_vector(ang):
    """ The so-called forward vector. """
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def shoot(self):
        global a_missile
        position_x = self.pos[0] + math.cos(self.angle)*self.radius
        position_y = self.pos[1] + math.sin(self.angle)*self.radius
        position = [position_x, position_y]
        forward = angle_to_vector(self.angle)
        velocity = [self.vel[0] + MISSILE_ACCEL_PARAM*forward[0], self.vel[1] + MISSILE_ACCEL_PARAM*forward[1]]
        
        a_missile = Sprite(position, velocity, 0, 0, missile_image, missile_info, missile_sound)
        
        
    def draw(self,canvas):
        if not self.thrust:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
            ship_thrust_sound.rewind()
        else:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]], self.image_size, self.pos, self.image_size, self.angle)
            ship_thrust_sound.play()
            
    def update(self):
        self.angle += self.angle_vel
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        # screen wrap
        if self.pos[0] < 0 or self.pos[0] > WIDTH:
            self.pos[0] %= WIDTH
        if self.pos[1] < 0 or self.pos[1] > HEIGHT:
            self.pos[1] %= HEIGHT
        
        self.vel[0] *= (1-FRICTION_PARAM)
        self.vel[1] *= (1-FRICTION_PARAM)
        
        forward = angle_to_vector(self.angle)
        if self.thrust:
            self.vel[0] += SHIP_ACCEL_PARAM * forward[0]
            self.vel[1] += SHIP_ACCEL_PARAM * forward[1]
        
                
class Sprite:
    """ Used for rocks and missiles. """
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        # next week: if self.lifespan do not show 
    
    def update(self):
        self.angle += self.angle_vel

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        if self.pos[0] < 0 or self.pos[0] > WIDTH:
            self.pos[0] %= WIDTH
        if self.pos[1] < 0 or self.pos[1] > HEIGHT:
            self.pos[1] %= HEIGHT

           
def draw(canvas):
    global time
    
    # animate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, [center[0] - wtime, center[1]], [size[0] - 2 * wtime, size[1]], 
                                [WIDTH / 2 + 1.25 * wtime, HEIGHT / 2], [WIDTH - 2.5 * wtime, HEIGHT])
    canvas.draw_image(debris_image, [size[0] - wtime, center[1]], [2 * wtime, size[1]], 
                                [1.25 * wtime, HEIGHT / 2], [2.5 * wtime, HEIGHT])

    # draw ship and sprites
    my_ship.draw(canvas)
    my_ship.update()
    a_rock.draw(canvas)
    a_rock.update()
    if a_missile:
        a_missile.draw(canvas)
        a_missile.update()
        
    # draw lives and score
    canvas.draw_text('Lives: ' + str(lives), (1, 20), 25, "Red")
    canvas.draw_text('Score: ' + str(score), (WIDTH - 100, 20), 25, "Red")

    
            
def rock_spawner():
    """ 
    Spawns a new rock every 1 sec
    in a random position, velocity, direction, spin. 
    """
    global a_rock
    
    pos = [random.randrange(WIDTH), random.randrange(HEIGHT)]
    vel_x = random.randrange(1, 5)
    vel_y = random.randrange(1, 4)
    direction = random.randrange(4) # to get all possible directions
    if direction == 0:
        vel = [vel_x, vel_y]
    elif direction == 1:
        vel = [vel_x, -vel_y]
    elif direction == 2:
        vel = [-vel_x, vel_y]
    elif direction == 3:
        vel = [-vel_x, -vel_y]
        
    direction = random.randrange(2) # random spin direction    
    angle_vel = random.randrange(3) / 10
    
    a_rock = Sprite(pos, vel, 0, angle_vel if direction == 0 else -angle_vel, asteroid_image, asteroid_info)
    
    
def keydown(key):
    global my_ship
    if key == simplegui.KEY_MAP['up']:
        my_ship.thrust = True
    elif key == simplegui.KEY_MAP['left']:
        my_ship.angle_vel = -SHIP_ANGLE_VEL 
    elif key == simplegui.KEY_MAP['right']:
        my_ship.angle_vel = SHIP_ANGLE_VEL
    elif key == simplegui.KEY_MAP["space"]:
        my_ship.shoot()
        
        
def keyup(key):
    global my_ship
    if key == simplegui.KEY_MAP['up']:
        my_ship.thrust = False
    elif key == simplegui.KEY_MAP['left']:
        my_ship.angle_vel = 0
    elif key == simplegui.KEY_MAP['right']:
        my_ship.angle_vel = 0

    
# initialize frame with handlers 
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0.1, asteroid_image, asteroid_info)
a_missile = None

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

timer = simplegui.create_timer(1000.0, rock_spawner)
timer.start()
frame.start()
