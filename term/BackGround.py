from pico2d import *
import game_framework
import random

class BackGround:
    def __init__(self):
        BackGround.image = load_image('./res/map.png')

    def update(self):
        pass
        
    def draw(self):
        self.image.draw(400,300)



