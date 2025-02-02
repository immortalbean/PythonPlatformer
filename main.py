print("Python Platformer - Version 1.0")

import pygame
import os; os.chdir(os.path.dirname(__file__))
import render
import mathoperations
import player
import gameplay

pygame.init()
resolution = (1280, 720)
screen = pygame.display.set_mode(resolution)
running = True
clock = pygame.time.Clock()
camera = gameplay.Camera()

player = player.Player()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)
    player.tick(0, camera)
    render.render_level(screen, 0, camera, resolution, player)
