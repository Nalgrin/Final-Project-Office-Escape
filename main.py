import pgzrun
import pygame
import random
from pgzero.actor import Actor 
WIDTH = 1024
HEIGHT = 768

GAME_STATE_TITLE = 0
GAME_STATE_INIT = 1
GAME_STATE_PLAYING = 2
GAME_STATE_FAILED = 3

red = (212, 47, 47)
white = (255, 255, 255)

floor = HEIGHT - 100

background = Actor("background", anchor=('left', 'top'))
title = Actor("title", anchor=('left', 'top'))

player = Actor("player", anchor=('center', 'bottom'))
player.x = 200
player.y = floor
gravity = 0.8

boss = Actor("boss", anchor=('center', 'bottom'))
boss.x = 25
boss.y = floor


stapler = Actor("stapler")
stapler.x = random.randint(900, 5000)
stapler.y = 490

lamp = Actor("lamp")


desks = []

class GameState:
    state = None    
    next_desk_spawn_time = pygame.time.get_ticks()
    background_x_offset = 0
    next_lamp_spawn_time = pygame.time.get_ticks()
    health = 0
    score = 0


game_state = GameState()
game_state.state = GAME_STATE_TITLE

def spawn_desk():
    desk = Actor("desk", anchor=('center', 'bottom'))
    desk.x = WIDTH + 25
    desk.y = floor
    desks.append(desk)

def init_game():
    desks.clear()
    game_state.next_desk_spawn_time = pygame.time.get_ticks()
    player.player_y_velocity = 0
    player.y = floor
    spawn_desk()
    game_state.state = GAME_STATE_PLAYING
    game_state.health = 3
    game_state.score = 0 
    lamp.x = random.randint(900, 5000)
    lamp.y = 620
    music.play("playing")

def game_end():
    game_state.state = GAME_STATE_FAILED
    sounds.failed.play()        

def update(): 
    
    if game_state.state == GAME_STATE_INIT:
        init_game()

    if game_state.state == GAME_STATE_PLAYING:
        if keyboard.space:
            if player.y == floor:
                player.player_y_velocity = 25
                sounds.jump.play()
 
        if game_state.next_desk_spawn_time < pygame.time.get_ticks():
            spawn_desk()
            game_state.next_desk_spawn_time = pygame.time.get_ticks() + (random.randint(1,5) * 1000)
        
        player.y = player.y - player.player_y_velocity

        if player.y > floor:
            player.y = floor
            player.player_y_velocity = 0
        
        if player.y < floor:
            player.player_y_velocity = player.player_y_velocity - gravity 

        update_desks = desks.copy()

        for desk in update_desks:
            desk.x = desk.x - 5
            if desk.right < 0:
                desks.remove(desk)
            
            if player.colliderect(Rect(desk.left+20, desk.top+20, desk.width-40, desk.height-20)):
                game_end()

        game_state.background_x_offset = game_state.background_x_offset - 3
        if game_state.background_x_offset < -WIDTH: 
            game_state.background_x_offset += WIDTH
        
        stapler.x -= 5

        if stapler.x < -50:
            stapler.x = random.randint(900, 5000)
            stapler.y = 490

        if player.colliderect(stapler):
            sounds.stapler.play()
            stapler.x = random.randint(900, 5000)
            stapler.y = 490
            game_state.score += 5

        lamp.x -=5

        if lamp.x < -50:
            lamp.x = random.randint(900, 5000)
            lamp.y = 620
        
        if player.colliderect(Rect(lamp.left+10, lamp.top+10, lamp.width-10, lamp.height-10)):
            sounds.lamp.play()
            lamp.x = random.randint(900, 5000)
            lamp.y = 620
            game_state.health -= 1

        if game_state.health == 0:
            game_end()

    if game_state.state == GAME_STATE_FAILED:
        music.fadeout(1)
        if keyboard.RETURN:
            game_state.state = GAME_STATE_INIT
        if keyboard.escape:
            quit()

    if game_state.state == GAME_STATE_TITLE:
        if keyboard.RETURN:
            game_state.state = GAME_STATE_INIT
    

    
    


def draw():
    if game_state.state == GAME_STATE_TITLE:
        title.draw()
        screen.draw.text("Office Escape", (300, 100), color="white", owidth=1.5, ocolor="black", fontname="hemi head bd it.otf", fontsize=70, align="center")
        screen.draw.textbox("How You Play: \nJump over the desks so you don't lose.\n If you hit a lamp you lose one of your lives\n Make sure to collect those staplers you see to gain points", Rect(0, 200, WIDTH, HEIGHT-400), color="yellow", owidth=1.0, ocolor="black", fontname="hemi head bd it.otf", align="center")
        screen.draw.text("Press enter to start",  (300, 600), color="yellow", owidth=1.0, ocolor="black", fontname="hemi head bd it.otf", fontsize=30, align="center")
        return

    background.x = game_state.background_x_offset
    background.draw()
    background.x = game_state.background_x_offset + WIDTH
    background.draw()


    screen.draw.filled_rect(Rect(0,floor, WIDTH,HEIGHT-floor), (128, 128, 128))
    player.draw()
    for desk in desks:
        desk.draw()
    stapler.draw()
    lamp.draw()
    boss.draw()

    if game_state.state == GAME_STATE_PLAYING:
        screen.draw.text("Score: " + str(game_state.score), (40, 40), color="white", fontname="hemi head bd it.otf", fontsize=30, owidth=1.0, ocolor="black")
        screen.draw.text("Health: " + str(game_state.health), (840, 40), color="white", fontname="hemi head bd it.otf", fontsize=30, owidth=1.0, ocolor="black")

    if game_state.state == GAME_STATE_FAILED:
        screen.draw.text("You failed to escape", centerx=500, centery=110, color="yellow", fontname = "hemi head bd it.otf", fontsize = 80, owidth=1.0, ocolor="black")
        screen.draw.text("Final Score\n" + str(game_state.score), centerx=500, centery=350, color="white", fontname = "hemi head bd it.otf", fontsize = 60, owidth=1.0, ocolor="black")
        screen.draw.text("Press ENTER to try again or ESC to quit", centerx=500, centery=490, color="yellow", fontname = "hemi head bd it.otf", fontsize = 30, owidth=1.0, ocolor="black")


pgzrun.go()