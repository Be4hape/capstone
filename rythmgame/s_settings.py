# settings.py
import pygame

# 전역 변수 선언
WHITE = (255, 255, 255)
size = (1300, 700)
screen = pygame.display.set_mode(size)
score = 0
font_test = pygame.font.SysFont(None, 100)
button_font = pygame.font.SysFont(None, 75)

# 게임 상태 관리
game_state = 'menu'

# 맵 정보
maps = ["Map 1", "Map 2", "Map 3"]
current_map = None