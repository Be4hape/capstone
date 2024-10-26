# settings.py
import pygame
from s_image_loader import load_images

# Pygame 초기화
pygame.init()

# 전역 변수 선언
WHITE = (255, 255, 255)

# 화면 크기 설정
size = (1300, 700)

# 버튼 크기 설정
START_BUTTON_SIZE = (300, 100)
RESUME_BUTTON_SIZE = (300, 100)
OPTIONS_BUTTON_SIZE = (300, 100)
EXIT_BUTTON_SIZE = (300, 100)

# 화면 설정
screen = pygame.display.set_mode(size)

# 점수와 폰트 설정
score = 0
font_test = pygame.font.SysFont(None, 100)
button_font = pygame.font.SysFont(None, 75)

# 게임 상태 관리
game_state = 'menu'

#게임 종료 여부
done = False

# 프레임 속도 제어를 위한 clock 객체 초기화
clock = pygame.time.Clock()

# 맵 정보
maps = ["Map 1", "Map 2", "Map 3"]
current_map = None


images = load_images(size[0], size[1])

shape_scale = (100, 100)
dot_scale = (100, 100)

images['shape'] = pygame.transform.scale(images['shape'], shape_scale)
images['dot'] = pygame.transform.scale(images['dot'], dot_scale)


