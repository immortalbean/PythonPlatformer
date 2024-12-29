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

player = player.Player(pygame.Vector2(30, 50))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #player.tick()
    clock.tick(60)
    screen.fill((20, 20, 30))
    #Create system to preload level data, rather than reading the file every frame
    player.tick("level/level_1.json")
    camera_position = pygame.Vector2(mathoperations.lerp(camera_position.x, player.position.x, 0.2), mathoperations.lerp(camera_position.y, player.position.y, 0.2))
    player.draw(screen, camera_position, resolution)
    render.render_level(screen, "level/level_1.json", camera_position, resolution)
    pygame.display.flip()
