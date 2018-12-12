from pico2d import *
import game_framework
import random

global MouseX , MouseY

class  Player:
    def __init__(self):
        print("Creating..")
        global MouseX, MouseY
        MouseX, MouseY = 150,150
        self.x = 150;
        self.y = 150;
        self.image = load_image('./res/Playermap.png')
        self.frame = 0
        self.top = 35
        self.bottom = 30
        self.right = 25
        self.left = 15
        self.dir = 1;
        self.speed = 5;

    def draw(self):
        if self.dir == 1: 
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        draw_rectangle(self.x-self.left,self.y-self.bottom,self.x+self.right,self.y+self.top)

    def update(self):
        global MouseX,MouseY
        self.frame = (self.frame + 1) % 5
        lengthX = MouseX - self.x
        lengthY = MouseY - self.y
        dist = math.sqrt(lengthX ** 2 + lengthY ** 2) 

        if lengthX < 0:
            PathX = -1
        elif lengthX > 0:
            PathX = 1
        else:
            PathX = 0
            
        if lengthY < 0:
            PathY = -1
        elif lengthY > 0:
            PathY = 1
        else:
            PathY = 0

        if dist > 5:
            self.x += self.speed * lengthX/ dist 
            self.y += self.speed * lengthY/ dist
        else:
             self.x = MouseX
             self.y = MouseY
        if(MouseX < self.x):
            self.dir = -1
        else:
            self.dir = 1


    def handle_events(self,e):
        global MouseX,MouseY
        for event in e:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    game_framework.pop_state()
            elif event.type == SDL_MOUSEMOTION:
                 pass
            elif event.type == SDL_MOUSEBUTTONDOWN:
                MouseX,MouseY = event.x, get_canvas_height() - event.y
            




