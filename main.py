import pygame
print('setup start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')
print('Loop Start')
while True:
    for event in pygame.event.get(): #Check for all events
        if event.type == pygame.QUIT:
            pygame.quit()#Close Window
            quit() # end pygame