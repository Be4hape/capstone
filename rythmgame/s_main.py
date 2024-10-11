# main.py
import pygame
import random
from s_settings import *
from s_image_loader import load_images
from s_utils import draw_button, is_button_clicked

pygame.init()

# 이미지 로딩
images = load_images()

class Dot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = images['dot']
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 400
        self.speed_x = -10
        self.speed_y = 0

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x < 100:
            self.kill()

    def remove(self):
        global score
        if 150 <= self.rect.x <= 250:
            score += 1
            self.kill()

def runGame():
    global done, score, game_state, current_map

    all_sprites = pygame.sprite.Group()
    start_time = pygame.time.get_ticks()
    spawn_times = []

    while not done:
        clock.tick(60)
        screen.fill(WHITE)

        if game_state == 'menu':
            if 'main' in images:
                screen.blit(images['main'], (0, 0))
            draw_button("Start Game", 500, 300, 300, 100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos, 500, 300, 300, 100):
                        game_state = 'map'

        elif game_state == 'map':
            if 'choosemap' in images:
                screen.blit(images['choosemap'], (0, 0))
            for i, map_name in enumerate(maps):
                draw_button(map_name, 200 + i * 350, 300, 300, 100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, map_name in enumerate(maps):
                        if is_button_clicked(mouse_pos, 200 + i * 350, 300, 300, 100):
                            current_map = map_name
                            if current_map == "Map 1":
                                from map1 import spawn_times
                            elif current_map == "Map 2":
                                from map2 import spawn_times
                            elif current_map == "Map 3":
                                from map3 import spawn_times
                            game_state = 'game'
                            start_time = pygame.time.get_ticks()

        elif game_state == 'game':
            current_time = pygame.time.get_ticks() / 1000
            for spawn_time in spawn_times:
                if current_time >= spawn_time and len(all_sprites) < 10:
                    dot = Dot()
                    all_sprites.add(dot)
                    spawn_times.remove(spawn_time)
                    break

            all_sprites.update()
            all_sprites.draw(screen)
            text = font_test.render(str(score), True, (0, 0, 0))
            screen.blit(text, (100, 100))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                for dot in all_sprites:
                    dot.remove()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_state = 'pause'
            if 'shape' in images:
                screen.blit(images['shape'], (205, 395))

        elif game_state == 'pause':
            draw_button("Resume", 500, 200, 300, 100)
            draw_button("Options", 500, 350, 300, 100)
            draw_button("Exit", 500, 500, 300, 100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos, 500, 200, 300, 100):
                        game_state = 'game'
                    elif is_button_clicked(mouse_pos, 500, 350, 300, 100):
                        print("Options clicked")
                    elif is_button_clicked(mouse_pos, 500, 500, 300, 100):
                        done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_state = 'game'

        pygame.display.update()

runGame()
pygame.quit()
