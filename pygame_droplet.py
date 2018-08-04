# droplet animation
import pygame

pygame.init()

panel_width = 300
panel_height = 300

# square characteristics
width = 25
height = 25
x = (panel_width / 2) - 20
y = (panel_height / 2) - 20

# slide length
slide_height = 35
slide = False
offset_x = 0
offset_y = 0

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 215, 0)
black = (0, 0, 0)

running = True

clock = pygame.time.Clock()

root = pygame.display.set_mode((panel_width, panel_height))
pygame.display.set_caption("droplet")

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if not sliding then slide
    if slide == False and offset_x == 0 and offset_y == 0:
        slide = True

    # going up
    if slide:
        offset_y += .75
        offset_x += .75
        if offset_y >= slide_height:  # reached max height
            slide = False

    # going down
    elif offset_y > 0 and slide == False:
        offset_y -= .75
        offset_x -= .75

    root.fill(black)

    pygame.draw.rect(
        root,
        red,
        (x + offset_x,
         y - offset_y,
         width,
         height))  # top right
    pygame.draw.rect(
        root,
        green,
        (x + offset_x,
         y + offset_y,
         width,
         height))  # bottom right
    pygame.draw.rect(
        root,
        blue,
        (x - offset_x,
         y - offset_y,
         width,
         height))  # top left
    pygame.draw.rect(
        root,
        yellow,
        (x - offset_x,
         y + offset_y,
         width,
         height))  # bottom left
    pygame.display.update()

    clock.tick(60)

pygame.quit()
