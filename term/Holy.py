from pico2d import * # C:\Users\enjcat\AppData\Local\Programs\Python\Python36\lib\site-packages\pico2d
import game_framework
import random
import game_world
import random
import Wepon


dicts = {0:Wepon.stick(),1:Wepon.sword(),2:Wepon.ice(),3:Wepon.fire(),4:Wepon.wand(),5:Wepon.heal()}

class Tower:
    def __init__(self):
        print("Creating..")
        self.image = load_image('./res/popmap.png')
        self.x = 150
        self.y = 150
        self.frame = 0
        self.speed = 3
        self.on = 0
    def draw(self):
        self.image.clip_draw(int(self.frame) * 200, 0, 200, 200, self.x, self.y)
    def update(self):
        if(self.on == 1):
            self.frame = self.frame + 0.2
            if self.frame >= 4:
                self.on = 0
                game_world.add_object(dicts[random.randint(0,5)],layer_obstacle)
        if(self.on == 0 and self.frame > 0):
            self.frame -= 0.2

    def pop(self):
        self.on = 1


        




