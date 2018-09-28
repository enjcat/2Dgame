from pico2d import *
import random

class Grass:
    def __init__(grass_):
        grass_.image = load_image('./grass.png')
        print(grass_.image)
    def draw(grass_):
        grass_.image.draw(400, 300)

class Boy:
    def __init__(self):
        print("Creating..")
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.speed = random.uniform(1.0, 5.0)
        self.frame = random.randint(0, 7)
        self.image = load_image('./run_animation.png')
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 8
        global gloX, gloY

        lengthX = gloX - self.x
        lengthY = gloY - self.y 

        if lengthX < 0:
            PathX = -1
        else:
            PathX = 1
            
        if lengthY < 0:
            PathY = -1
        else:
            PathY = 1

        self.x += self.speed * PathX
        self.y += self.speed * PathY

        if lengthX*PathX < self.speed:
            self.x = gloX
        if lengthY*PathY < self.speed:
            self.y = gloY


def handle_events():
    global running
    global gloX,gloY
    global index
    global DirList
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_MOUSEMOTION:
             gloX,gloY = event.x, 600 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            DirList[index] = (event.x,600-event.y)
            index += 1
        
            
open_canvas()

running = True

gloX,gloY = 0,0

Grass_ = Grass()

boys = [ Boy() for i in range(20) ]

while running:
    handle_events()

    for boy in boys:
        boy.update()

    clear_canvas()
    Grass_.draw()
    for boy in boys:
        boy.draw()
    update_canvas()

    delay(0.05)

close_canvas()


