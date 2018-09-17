from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character_down = load_image('run_down.png')
character_right = load_image('run_right.png')
character_up = load_image('run_up.png')
character_left = load_image('run_left.png')
frame = 0
x = 0

while (1):
    while (x < 800):
        clear_canvas()
        grass.draw(400, 30)
        character_down.clip_draw(frame * 100, 0, 100, 100, 400 + 100*cos(radians(x)), 300 + 100*sin(radians(x)))
        frame = (frame + 1) % 8
        update_canvas()
        x = (x + 10)%361
        delay(0.05)
        get_events()



close_canvas()
