import pygame
import random

pygame.init()

# 전역변수 선언
WHITE = (255, 255, 255)
size = (1300, 700)
screen = pygame.display.set_mode(size)
score = 0
font_test = pygame.font.SysFont(None, 100)

done = False
clock = pygame.time.Clock()

shape = pygame.image.load('shape.png')

class Dot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('dot.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 400
        self.speed_x = -10
        self.speed_y = 0

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # x 좌표가 100 미만이 되면 Dot 객체 제거
        if self.rect.x < 100:
            self.kill()

    def remove(self):
        global score
        # x 좌표가 150과 250 사이에 있으면 Dot 객체 제거
        if 150 <= self.rect.x <= 250:
            score += 1
            self.kill()

def runGame():
    global done, score

    all_sprites = pygame.sprite.Group()
    start_time = pygame.time.get_ticks()

    spawn_times = [3.0, 3.7, 4.0, 4.7, 5.4, 5.7, 6.4, 6.9, 7.3, 7.8, 8.2, 8.7, 9.1,
                   9.8, 10.2, 10.8, 11.5, 12.2, 12.7, 13.1, 13.6, 14.1, 14.8, 15.5,
                   15.8, 16.5, 17.2, 17.5, 18.2, 18.7, 19.1, 19.6, 20.0, 20.5, 20.9,
                   21.6, 22.0, 22.6, 23.3, 24.0, 24.5, 24.9, 25.4, 25.9, 26.6, 27.3,
                   27.6, 28.3, 29.0, 29.3, 30.0, 30.5, 30.9, 31.4, 31.8, 32.3, 32.7,
                   33.4, 33.8, 34.4, 35.1, 35.8, 36.3, 36.7, 37.2, 37.7, 38.4, 39.1,
                   39.4, 40.1, 40.8, 41.1, 41.8, 42.3, 42.7, 43.2, 43.6, 44.1, 44.5, 45.2, 45.6, 46.2, 46.9, 47.6, 48.1, 48.5, 49.0, 49.5]

    while not done:
        clock.tick(60)
        screen.fill(WHITE)

        # 지정된 시간마다 Dot 객체 생성
        current_time = pygame.time.get_ticks() / 1000
        for spawn_time in spawn_times:
            if current_time >= spawn_time and len(all_sprites) < 10:
                dot = Dot()
                all_sprites.add(dot)
                spawn_times.remove(spawn_time)
                break

        # 모든 Dot 객체 업데이트 및 화면에 그리기
        all_sprites.update()
        all_sprites.draw(screen)
        text = font_test.render(str(score), True, (0, 0, 0))
        screen.blit(text, (100, 100))

        # 스페이스바를 눌렀을 때 Dot 객체 제거
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            for dot in all_sprites:
                dot.remove()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
        screen.blit(shape, (205, 395))
        pygame.display.update()

runGame()
pygame.quit()
