import pygame

from code.menu import Menu


#!/usr/bin/python
# -*- coding: utf-8 -*-

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            # for event in pygame.event.get():  # Check for all events
            #     if event.type == pygame.QUIT:
            #         pygame.quit()  # Close Window
            #         quit()  # end pygame