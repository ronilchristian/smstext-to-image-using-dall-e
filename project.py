import image
import os
import pygame
import text
import time

# initializing Pygame
pygame.init()

# screen to display the text
projector_screen_index = 0

# get the size of the projecion screen
sizes = pygame.display.get_desktop_sizes()
screen_width, screen_height = sizes[projector_screen_index]

# setting up the display on the projector screen
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN, display=projector_screen_index)

# loading the background image
image_path = os.path.join(os.path.dirname(os.path.abspath('__file__')), 'images')
background_image = pygame.image.load(f"{image_path}/default.jpg")
# background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# setting the background color
background_color = (0, 0, 0)

# setting the font for the text
font_size = 30
font = pygame.font.Font(None, font_size)

# setting the text content and color
text_content = "your text will display here"
text_color = (255, 255, 255)

# creating a text surface
text_surface = font.render(text_content, True, text_color)

# Calculate the position to center the text on the screen
text_x = (screen_width - text_surface.get_width()) // 2
text_y = screen_height // 8

# calculate the position to center the image on the screen
image_x = (screen_width - background_image.get_width()) // 2
image_y = (screen_height - background_image.get_height()) // 2

# main loop
running = True
while running:
    screen.fill(background_color)
    screen.blit(background_image, (image_x, image_y))

    # Blit the text surface onto the screen
    screen.blit(text_surface, (text_x, text_y))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # updating the display
    pygame.display.flip()

    new_text = text.get_message()
    if new_text and new_text != text_content:
        text_content = new_text
        text_surface = font.render(text_content, True, text_color)
        text_x = (screen_width - text_surface.get_width()) // 2
        text_y = screen_height // 8
        try:
            background_image = pygame.image.load(image.generate_image(text_content))
            background_image = pygame.transform.scale(background_image, (512,512))
            image_x = (screen_width - background_image.get_width()) // 2
            image_y = (screen_height - background_image.get_height()) // 2
        except:
            msg_fail = "falied to load the image"
            msg_surface = font.render(msg_fail, True, text_color)
            text_x = (screen_width - text_surface.get_width()) // 2
            text_y = (screen_height - text_surface.get_height()) // 2
    else:
        text_content = "your text will display here"
        text_surface = font.render(text_content, True, text_color)
        text_x = (screen_width - text_surface.get_width()) // 2
        text_y = screen_height // 8
        background_image = pygame.image.load(f"{image_path}/default.jpg")
        image_x = (screen_width - background_image.get_width()) // 2
        image_y = (screen_height - background_image.get_height()) // 2

    # 5 second delay
    time.sleep(5)

# Quit Pygame
pygame.quit()
