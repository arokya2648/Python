import pygame
import random
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72
pygame.init()
background_image= pygame.tranform.scale(pygame.image.load('tutrle.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Sysfont('Times New Roman', FONT_SIZE)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super() .__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image, color, pygame.rect(0, 0, width, height))
        self.rect=self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x=max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)
screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN HEIGHT))
pygame.display.set_caption('sprite collision')
all_sprites = pygame.sprite.Group()
sprite1 = Sprite(pygame.color('black'), 20, 30)
sprite1.rect.x, sprite1.rect.y = random.randit(0 SCREEN_WIDTH - sprite1.rect.width), random.randit(0, SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)
sprite2 = Sprite(pygame.color('red'), 20, 30)
sprite2.rect.x, sprite2.rect.y = random.randit(0 SCREEN_WIDTH - sprite2.rect.width), random.randit(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)
running, won = True, False
clock =pygame.time.Clock()
while running:
    for event in pygame.event.get () :
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

        if 