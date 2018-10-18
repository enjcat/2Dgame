from pico2d import *
import game_framework
import random

class Grass:
    def __init__(grass_):
        grass_.image = load_image('./map.png')
        print(grass_.image)
    def draw(grass_):
        grass_.image.draw(750, 500)


class  Player:
    def __init__(self):
        print("Creating..")
        self.x = 750;
        self.y = 500;
        self.image = load_image('./Playermap.png')
        self.frame = 0
    def draw(self):
        self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 5

class Monster:
    def __init__(self):
        print("Creating..")
        self.x = 400;
        self.y = 300;
        self.image = load_image('./Playermap.png')
        self.frame = 0
    def draw(self):
        self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 5
    
        
        



def handle_events():
    global running
    global gloX,gloY
    global index
    global DirList
    global boys
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()
        elif event.type == SDL_MOUSEMOTION:
             gloX,gloY = event.x, 600 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            DirList.append(Dot(event.x, 600-event.y))
            index += 1




def enter():
    global Grass_ob
    global Player_ob
    open_canvas(1500,1000)
    Grass_ob = Grass()
    Player_ob = Player()

def update():
    global Player_ob
    Player_ob.update()

def draw():
    global Grass_ob
    global Player_ob
    delay(0.03)
    clear_canvas()
    Grass_ob.draw()
    Player_ob.draw()
    update_canvas()


def exit():
    close_canvas()

def pause():
    pass

def resume():
    pass


if __name__ == '__main__':
    import sys
    game_framework.run(sys.modules[__name__])
