import pygame

import scene

pygame.init()
pygame.display.set_caption("physics")

screen : pygame.Surface = pygame.display.set_mode((640, 360))

running = True

curScene = scene.Scene(640, 360)

clock = pygame.time.Clock()

fps = 200

while running:
    deltaTime = clock.tick(fps) / 1000

    events = []
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        else:
            events.append(event)

    
    curScene.update(deltaTime, events)
    curScene.render(screen)

    pygame.display.flip()

pygame.quit()