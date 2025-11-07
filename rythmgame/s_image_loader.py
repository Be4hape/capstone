# image_loader.py
import pygame

def load_images(screen_width=None, screen_height=None):
    images = {}
    #이미지 로드
    try:
        images['shape'] = pygame.image.load('C:/Users/solb/Desktop/capstone/Image_sample/배경/shape_resized.png')
        images['dot'] = pygame.image.load('C:/Users/solb/Desktop/capstone/Image_sample/배경/nb_resized.png')
        images['main'] = pygame.image.load('C:/Users/solb/Desktop/capstone/Image_sample/배경/메인화면_resized.png')
        images['choosemap'] = pygame.image.load('C:/Users/solb/Desktop/capstone/Image_sample/배경/맵선택_resized.png')
        images['ingameback'] = pygame.image.load('C:/Users/solb/Desktop/capstone/Image_sample/배경/인게임배경_resized.png')


        ##if screen_width and screen_height:
        ##    for key, image in images.items():
        ##        images[key] = scale_image_keep_aspect_ratio(image, screen_width, screen_height)
            
    except pygame.error as e:
        print(f"Could not load an image: {e}")
    
    return images


##def scale_image_keep_aspect_ratio(image, max_width, max_height):
    original_width, original_height = image.get_size()
    ratio = min(max_width / original_width, max_height / original_height)
    new_width = int(original_width * ratio)
    new_height = int(original_height * ratio)
    return pygame.transform.scale(image, (new_width, new_height))




