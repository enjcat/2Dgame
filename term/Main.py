from pico2d import *
import game_framework
import random
import game_world
import Monster
import player
import BackGround
import Holy


def handle_events():
    global Angel
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()
        elif event.type == SDL_MOUSEMOTION:
             Angel.handle_events(events)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            pass
            




def enter():
    global Angel
    open_canvas(300,300)
    bg = BackGround.BackGround()
    Angel = player.Player()
    tower = Holy.Tower()
    game_world.add_object(bg,game_world.layer_bg)
    game_world.add_object(Angel,game_world.layer_player)
    game_world.add_object(tower,game_world.layer_obstacle)

def update():
    delay(0.03)
    if(game_world.count_at_layer(game_world.layer_obstacle) < get_time()/10):
         game_world.add_object(Monster.Imp(),game_world.layer_obstacle)
         game_world.add_object(Monster.Tums(),game_world.layer_obstacle)
         game_world.add_object(Monster.Demon(),game_world.layer_obstacle)
         
    game_world.update()

def draw():
    clear_canvas()
    game_world.draw()
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
