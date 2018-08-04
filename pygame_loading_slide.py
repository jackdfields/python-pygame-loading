# loading
import pygame
import time

# component dimensions
x = 160
y = 225 

width = 25
height = 25

slide_height = 25
slide = False
offset_y = 0

# initialize window
pygame.init()
# window size
root = pygame.display.set_mode((500, 500))

pygame.display.set_caption("loading")

running = True

clock = pygame.time.Clock()

# run program
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if not sliding slide
    if slide == False and offset_y == 0:
        slide = True
    # going up
    if slide:
        offset_y += .75
        if offset_y >= slide_height:  # reached max height
            slide = False

    # going down
    elif offset_y > 0 and slide == False:
        offset_y -= .75

    root.fill((255, 255, 255))
    # R,G,B color values
    pygame.draw.rect(root, (255, 0, 0), (x, y - offset_y, width, height))
    pygame.draw.rect(root, (0, 255, 0), (x + 50, y + offset_y, width, height))
    pygame.draw.rect(root, (0, 0, 255), (x + 100, y - offset_y, width, height))
    pygame.draw.rect(root, (255, 215, 0),
                     (x + 150, y + offset_y, width, height))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
