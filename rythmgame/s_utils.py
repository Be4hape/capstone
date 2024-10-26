# utils.py
import pygame
from s_settings import screen, button_font

#버튼 그리는 함수
def draw_button(text, x, y, size):
    width, height = size
    pygame.draw.rect(screen, (0, 255, 0), [x, y, width, height])
    button_text = button_font.render(text, True, (0, 0, 0))
    screen.blit(button_text, (x + 10, y + 10))

def is_button_clicked(mouse_pos, x, y, size):
    width, height = size
    return x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height



