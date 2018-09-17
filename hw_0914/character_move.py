from pico2d import *

open_canvas()

grass = load_image('grass.png')
character_down = load_image('run_down.png')
character_right = load_image('run_right.png')
character_up = load_image('run_up.png')
character_left = load_image('run_left.png')

frame = 0
x = 0
while (x < 800):
    clear_canvas()
    grass.draw(400, 30)
    character_down.clip_draw(frame * 100, 0, 100, 100, x, 90)
    frame = (frame + 1) % 8
    update_canvas()
    x = x + 10
    delay(0.05)
    get_events()

frame = 0
x = 0

while (x < 600):
    clear_canvas()
    grass.draw(400, 30)
    character_right.clip_draw(0, frame * 100, 100, 100, 770, x)
    frame = (frame + 1) % 8
    update_canvas()
    x = x + 10
    delay(0.05)
    get_events()

frame = 0
x = 0

while (x < 800):
    clear_canvas()
    grass.draw(400, 30)
    character_up.clip_draw(frame * 100, 0, 100, 100, 800-x, 570)
    frame = (frame + 1) % 8
    update_canvas()
    x = x + 10
    delay(0.05)
    get_events()

frame = 0
x = 0

while (x < 600):
    clear_canvas()
    grass.draw(400, 30)
    character_left.clip_draw(0, frame * 100, 100, 100, 30, 600-x)
    frame = (frame + 1) % 8
    update_canvas()
    x = x + 10
    delay(0.05)
    get_events()

close_canvas()
