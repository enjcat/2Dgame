from pico2d import *
import game_framework
import random

global MouseX, MouseY

class  Player:
    def __init__(self):
        print("Creating..")
        global MouseX, MouseY
        MouseX, MouseY = 300,400
        self.x = 400;
        self.y = 300;
        self.image = load_image('./res/Playermap.png')
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

    def update(self):
        global MouseX,MouseY
        self.frame = (self.frame + 1) % 5
        self.x ,self.y = MouseX,MouseY


    def handle_events(self,e):
        global MouseX,MouseY
        for event in e:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    game_framework.pop_state()
            elif event.type == SDL_MOUSEMOTION:
                 MouseX,MouseY = event.x, get_canvas_height() - event.y
            elif event.type == SDL_MOUSEBUTTONDOWN:
                a= 1
            




