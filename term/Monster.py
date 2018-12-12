from pico2d import * # C:\Users\enjcat\AppData\Local\Programs\Python\Python36\lib\site-packages\pico2d
import game_framework
import random
import game_world
import random



class Monster:
    def __init__(self):
        print("Creating..")
    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        else:
            self.image.clip_composite_draw(self.frame * 100, 0, 100, 100, 0, 'h', self.x, self.y)
    def update(self):
        Player_ob = game_world.objects_at_layer(game_world.layer_player)
        Player_ob = next(Player_ob, None)

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
        if(Player_ob.x < self.x):
            self.dir = 1
        else:
            self.dir = -1

        #colide
        if(self.dir == -1):
            left ,right = (self.x - self.right), (self.x + self.left)
        else:
            left ,right = (self.x - self.left), (self.x + self.right)
        if(Player_ob.dir == -1):
            Tleft ,Tright = (Player_ob.x - Player_ob.right), (Player_ob.x + Player_ob.left)
        else:
            Tleft ,Tright = (Player_ob.x - Player_ob.left), (Player_ob.x + Player_ob.right)

        if (left < Tright and right > Tleft and
            (self.y+self.top)  > (Player_ob.y-Player_ob.bottom) and 
            (self.y-self.bottom) < (Player_ob.y+Player_ob.top)):
            if dist > 0:
                self.x -= self.speed * lengthX/ dist *20
                self.y -= self.speed * lengthY/ dist *20
            



class Tums:
    def __init__(self):
        print("Creating..")
        Start_rocation(self)
        self.image = load_image('./res/Tums.png')
        self.frame = 0
        self.speed = 3
        self.top = 65
        self.bottom = 70
        self.right = 55
        self.left = 60
        self.dir = 1
    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 150, 0, 150, 150, self.x, self.y)
        else:
            self.image.clip_composite_draw(self.frame * 150, 0, 150, 150, 0, 'h', self.x, self.y)
        draw_rectangle(self.x-self.left,self.y-self.bottom,self.x+self.right,self.y+self.top)
    def update(self):
        self.frame = (self.frame + 1) % 5
        Monster.update(self)

class Demon:
    def __init__(self):
        print("Creating..")
        Start_rocation(self)
        self.image = load_image('./res/Demon.png')
        self.frame = 0
        self.speed = 6
        self.top = 80
        self.bottom = 80
        self.right = 35
        self.left = 40
        self.dir = 1
    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 100, 0, 100, 200, self.x, self.y)
        else:
            self.image.clip_composite_draw(self.frame * 100, 0, 100, 200, 0, 'h', self.x, self.y)
        self.frame = (self.frame + 1) % 2
        draw_rectangle(self.x-self.left,self.y-self.bottom,self.x+self.right,self.y+self.top)
    def update(self):
        Monster.update(self)

class Imp:
    def __init__(self):
        print("Creating..")
        Start_rocation(self)
        self.image = load_image('./res/Imp.png')
        self.frame = 0
        self.speed = 2
        self.top = 15
        self.bottom = 35
        self.right = 35
        self.left = 30
        self.dir = 1
    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        else:
            self.image.clip_composite_draw(self.frame * 100, 0, 100, 100, 0, 'h', self.x, self.y,100,100)
        self.frame = (self.frame + 1) % 5
        draw_rectangle(self.x-self.left,self.y-self.bottom,self.x+self.right,self.y+self.top)
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

def Start_rocation(self):
    field_width = get_canvas_width()
    field_height = get_canvas_height()

    side = random.randint(1, 4) # 1=top, 2=left, 3=bottom, 4=right
    if (side == 1): # top
        self.x, self.y = random.randint(0, field_width), 0

    if (side == 2): # left
        self.x, self.y = 0, random.randint(0, field_height)

    if (side == 3): # bottom
        self.x, self.y = random.randint(0, field_width), field_height

    if (side == 4): # right
        self.x, self.y = field_width, random.randint(0, field_height)




if __name__ == '__main__':
    import sys
    game_framework.run(sys.modules[__name__])
