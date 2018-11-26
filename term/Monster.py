from pico2d import * # C:\Users\enjcat\AppData\Local\Programs\Python\Python36\lib\site-packages\pico2d
import game_framework
import random



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
        
    
        
        




def update():
    global Monster_List
    for Monsters in Monster_List:
        Monsters.update()

def draw():
    global Monster_List
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
