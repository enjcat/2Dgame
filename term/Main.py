from pico2d import *
import game_framework
import random

class Grass:
    def __init__(grass_):
        grass_.image = load_image('./res/map.png')
        print(grass_.image)
    def draw(grass_):
        grass_.image.draw(400,300)


class  Player:
    def __init__(self):
        print("Creating..")
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

class Monster:
    def __init__(self):
        print("Creating..")
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
    def update(self):
        global Player_ob
        lengthX = Player_ob.x - self.x
        lengthY = Player_ob.y - self.y

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

        if dist > 0:
            self.x += self.speed * lengthX/ dist 
            self.y += self.speed * lengthY/ dist

class Tums:
    def __init__(self):
        print("Creating..")
        self.x = 400;
        self.y = 400;
        self.image = load_image('./res/Tums.png')
        self.frame = 0
        self.speed = 3
    def draw(self):
        self.image.clip_draw(self.frame * 150, 0, 150, 150, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 5
        Monster.update(self)

class Demon:
    def __init__(self):
        print("Creating..")
        self.x = 300;
        self.y = 400;
        self.image = load_image('./res/Demon.png')
        self.frame = 0
        self.speed = 6
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 200, self.x, self.y)
        self.frame = (self.frame + 1) % 2
    def update(self):
        Monster.update(self)

class Imp:
    def __init__(self):
        print("Creating..")
        self.x = 200;
        self.y = 400;
        self.image = load_image('./res/Imp.png')
        self.frame = 0
        self.speed = 2
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        self.frame = (self.frame + 1) % 5
    def update(self):
        Monster.update(self)
        
    
        
        



def handle_events():
    global MouseX,MouseY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()
        elif event.type == SDL_MOUSEMOTION:
             MouseX,MouseY = event.x, 600 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            a= 1
            




def enter():
    global Grass_ob
    global Player_ob
    global Monster_List
    global MouseX,MouseY
    MouseX,MouseY = 400,300
    open_canvas(800,600)
    Monster_List = []
    Grass_ob = Grass()
    Player_ob = Player()
    Monster_List.append(Imp())
    Monster_List.append(Tums())
    Monster_List.append(Demon())

def update():
    global Player_ob
    global Monster_List
    Player_ob.update()
    for Monsters in Monster_List:
        Monsters.update()

def draw():
    global Grass_ob
    global Player_ob
    global Monster_List
    delay(0.1)
    clear_canvas()
    Grass_ob.draw()
    Player_ob.draw()
    for Monsters in Monster_List:
        Monsters.draw()
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
