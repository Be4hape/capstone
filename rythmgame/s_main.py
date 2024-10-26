# main.py
import pygame
import random
from s_settings import *
from s_image_loader import load_images
from s_utils import draw_button, is_button_clicked
from s_settings import START_BUTTON_SIZE, RESUME_BUTTON_SIZE, OPTIONS_BUTTON_SIZE, EXIT_BUTTON_SIZE

pygame.init()

class Dot(pygame.sprite.Sprite):
    def __init__(self, shape_rect):
        super().__init__()
        self.image = images['dot']
        self.rect = self.image.get_rect()
        # 초기 위치 설정 (화면 내 위치)
        self.rect.centerx = 1300
        self.rect.centery = 345
        self.speed_x = -10
        self.speed_y = 0

        self.shape_rect = shape_rect

    def update(self):
        # 속도에 따라 위치 업데이트
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # 화면 밖으로 나가면 제거
        if self.rect.x < 0:
            self.kill()

    def check_collision(self):
        if 300 <= self.rect.centerx <= 400:
            return True
        return False

def runGame():
    global done, score, game_state, current_map

    all_sprites = pygame.sprite.Group()
    start_time = pygame.time.get_ticks()
    spawn_times = []

    # shape의 위치 설정
    shape_rect = images['shape'].get_rect()
    shape_rect.center = (400, 345)

    # 점수 초기화 및 텍스트 캐싱
    previous_score = -1
    score_text = font_test.render(str(score), True, (255, 255, 255))

    while not done:
        clock.tick(30)
        screen.fill(WHITE)

        if game_state == 'menu':
            if 'main' in images:
                screen.blit(images['main'], (0, 0))
            draw_button("Start Game", 500, 300, START_BUTTON_SIZE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos, 500, 300, START_BUTTON_SIZE):
                        game_state = 'map'

        elif game_state == 'map':
            if 'choosemap' in images:
                screen.blit(images['choosemap'], (0, 0))
            for i, map_name in enumerate(maps):
                draw_button(map_name, 200 + i * 350, 300, START_BUTTON_SIZE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, map_name in enumerate(maps):
                        if is_button_clicked(mouse_pos, 200 + i * 350, 300, START_BUTTON_SIZE):
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
            # 배경 그리기
            if 'ingameback' in images:
                screen.blit(images['ingameback'], (0, 0))

            # 모든 dot 객체 업데이트 및 화면에 그리기
            current_time = pygame.time.get_ticks() / 1000
            for spawn_time in spawn_times:
                if current_time >= spawn_time and len(all_sprites) < 10:
                    dot = Dot(shape_rect)
                    all_sprites.add(dot)
                    spawn_times.remove(spawn_time)
                    break

            all_sprites.update()
            all_sprites.draw(screen)


            for dot in all_sprites:
                if dot.check_collision():
                    score += 1
                    dot.kill()

            # 점수 텍스트를 변경될 때만 업데이트
            if score != previous_score:
                score_text = font_test.render(str(score), True, (255, 255, 255))
                previous_score = score

            # 점수 텍스트 그리기
            screen.blit(score_text, (100, 100))

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

            # shape의 위치를 업데이트하여 그리기
            screen.blit(images['shape'], shape_rect.topleft)

        elif game_state == 'pause':
            draw_button("Resume", 500, 200, RESUME_BUTTON_SIZE)
            draw_button("Options", 500, 350, OPTIONS_BUTTON_SIZE)
            draw_button("Exit", 500, 500, EXIT_BUTTON_SIZE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos, 500, 200, RESUME_BUTTON_SIZE):
                        game_state = 'game'
                    elif is_button_clicked(mouse_pos, 500, 350, OPTIONS_BUTTON_SIZE):
                        print("Options clicked")
                    elif is_button_clicked(mouse_pos, 500, 500, EXIT_BUTTON_SIZE):
                        done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_state = 'game'

        pygame.display.update()

runGame()
pygame.quit()
