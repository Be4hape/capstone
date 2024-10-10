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

# 이미지 경로 변경
shape = pygame.image.load('C:/Users/solb/Desktop/capstone/capstone/rythmgame/dot.png')
button_font = pygame.font.SysFont(None, 75)

# status로 게임 상태 구분, menu, map, game, pause 등
game_state = 'menu'

# 맵의 갯수 및 정보
maps = ["Map 1", "Map 2", "Map 3"]

current_map = None  # 선택된 맵

class Dot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 이미지 경로 변경
        self.image = pygame.image.load('C:/Users/solb/Desktop/capstone/capstone/rythmgame/dot.png')
        self.rect = self.image.get_rect()

        # 초기 위치 설정
        self.rect.x = 1200
        self.rect.y = 400

        # 속도 설정
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
        if 150 <= self.rect.x <= 250:
            score += 1
            self.kill()


# 버튼 생성 함수
def draw_button(text, x, y, width, height):
    pygame.draw.rect(screen, (0, 255, 0), [x, y, width, height])
    button_text = button_font.render(text, True, (0, 0, 0))
    screen.blit(button_text, (x + 10, y + 10))


# 버튼 클릭 감지 함수
def is_button_clicked(mouse_pos, x, y, width, height):
    return x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height


def runGame():
    global done, score, game_state, current_map

    all_sprites = pygame.sprite.Group()
    start_time = pygame.time.get_ticks()

    spawn_times = []

    while not done:
        clock.tick(60)
        screen.fill(WHITE)

        # 게임 상태가 메뉴일 때
        if game_state == 'menu':
            draw_button("Start Game", 500, 300, 300, 100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if is_button_clicked(mouse_pos, 500, 300, 300, 100):
                        game_state = 'map'  # 맵 선택 화면으로 이동

        # 맵 선택 화면
        elif game_state == 'map':
            # 가로로 버튼들을 나열하기 위해 각 버튼의 x 좌표 변경
            for i, map_name in enumerate(maps):
                draw_button(map_name, 200 + i * 350, 300, 300, 100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    for i, map_name in enumerate(maps):
                        if is_button_clicked(mouse_pos, 200 + i * 350, 300, 300, 100):
                            current_map = map_name  # 선택된 맵 저장
                            
                            # 각 맵 파일에서 악보 데이터를 가져옴
                            if current_map == "Map 1":
                                from map1 import spawn_times
                            elif current_map == "Map 2":
                                from map2 import spawn_times
                            elif current_map == "Map 3":
                                from map3 import spawn_times
                            
                            game_state = 'game'  # 게임 상태로 이동
                            start_time = pygame.time.get_ticks()  # 타이머 리셋

        # 게임 실행 상태일 때
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
                        game_state = 'pause'  # 일시정지 상태로 전환

            screen.blit(shape, (205, 395))

        # 게임 상태가 일시정지일 때
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
                        game_state = 'game'  # 게임 재개
                    elif is_button_clicked(mouse_pos, 500, 350, 300, 100):
                        print("Options clicked")
                    elif is_button_clicked(mouse_pos, 500, 500, 300, 100):
                        done = True  # 게임 종료

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_state = 'game'  # ESC를 다시 누르면 게임 재개

        pygame.display.update()


runGame()
pygame.quit()
