import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Key Events")

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            print(event.key) #窗口负责接收按键，终端负责显示结果

    screen.fill((230,230,230))
    pygame.display.flip()