# image_loader.py
import pygame

def load_images():
    images = {}
    #이미지 로드
    try:
        images['shape'] = pygame.image.load('C:/Users/solb/Desktop/capstone/capstone/rythmgame/shape.png')
        images['dot'] = pygame.image.load('C:/Users/solb/Desktop/capstone/capstone/rythmgame/dot.png')
        images['main'] = pygame.image.load('C:/Users/solb/Desktop/capstone/Image_sample/배경/메인화면.png')
        images['choosemap'] = pygame.image.load('C:/Users/solb/Desktop/capstone/Image_sample/배경/맵선택.png')


        if
        

    except pygame.error as e:
        print(f"Could not load an image: {e}")
    
    return images