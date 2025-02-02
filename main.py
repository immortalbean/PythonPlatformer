print("Python Platformer - Version 1.0")

import pygame
import os; os.chdir(os.path.dirname(__file__))
import render
import mathoperations
import player

pygame.init()
resolution = (1280, 720)
screen = pygame.display.set_mode(resolution)
running = True
clock = pygame.time.Clock()
camera_position = pygame.Vector2(0, 0)

player = player.Player()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)
    player.tick(0)
    camera_position = pygame.Vector2(mathoperations.lerp(camera_position.x, player.position.x, 0.2), mathoperations.lerp(camera_position.y, player.position.y - 100, 0.05))
    #Move the camera movement to the player.tick()
    render.render_level(screen, 0, camera_position, resolution, player)
