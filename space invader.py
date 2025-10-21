import math
import pygame
import random
SCREEN_WIDTH=800
SCREEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y=380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
COLLISION_DISTANCE=27
pygame.init()
screen=pygame.display.det_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background=pygame.image.load('background.png')
pygame.display.set_caption('Space invader')
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
playerlmg=pygame.image.load('player.png')
playerx=PLAYER_START_X
playery=PLAYER_START_Y
playerx_change=0
enemylmg=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
num_of_enemies=6
for _i in range(num_of_enemies):
    enemylmg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0, SCREEN_WIDTH-64))
    enemyy.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyx_change.append(ENEMY_SPEED_X)
    enemyy_change.sppend(ENEMY_SPEED_Y)
bulletlmg=pygame.image.load('bullet.png')
bulletx=0
bullety=PLAYER_START_Y
bulletx_change=0
bullety_change=BULLET_SPEED_Y
bullet_state='ready'
score_value=0
font=pygame.font.font('freesansbold.ttf', 32)
textx=10
texty=10
over_font=pygame.font.font('freesansbold.ttf', 64)
def show_score(x, y):
    score = font.render('Score:'+str(score_value))