from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image ('grass.png')
    def draw(self):
        self.image.draw(400, 30)

class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(100,600), 599
        self.frame = 0
        self.image = load_image('ball41x41.png')

    def update(self):
        self.frame =  random.randint(0,7)
        if(self.y >= 60):
            self.y -= random.randint(1,10)

    def draw(self):
        self.image.draw(self.x , self.y)

class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 600), 599
        self.frame = 0
        self.image = load_image('ball21x21.png')

    def update(self):
        self.frame = random.randint(0, 7)
        if (self.y >= 50):
            self.y -= random.randint(1, 10)

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

big_ball = BigBall()
small_ball = SmallBall()

big_balls = [BigBall() for i in range(10)]
small_balls = [SmallBall() for i in range(10)]
grass = Grass()

running = True
# game main loop code
while running:
    handle_events()
    for big_ball in big_balls:
        big_ball.update()

    for small_ball in small_balls:
        small_ball.update()

    clear_canvas()
    grass.draw()
    for big_ball in big_balls:
        big_ball.draw()

    for small_ball in small_balls:
        small_ball.draw()
    update_canvas()

    delay(0.05)
# finalization code
close_canvas