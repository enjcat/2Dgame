from pico2d import * # C:\Users\enjcat\AppData\Local\Programs\Python\Python36\lib\site-packages\pico2d
import game_framework
import random
import game_world
import random




class Tower:
    def __init__(self):
        print("Creating..")
        self.image = load_image('./res/popmap.png')
        self.x = 150
        self.y = 150
        self.frame = 0
        self.speed = 3
    def draw(self):
        self.image.clip_draw(self.frame * 200, 0, 200, 200, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 5


        




