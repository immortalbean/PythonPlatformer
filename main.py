print("Python Platformer - Version 1.1")

import pygame
import os; os.chdir(os.path.dirname(__file__))
import render
import mathoperations
import gameplay
import json

pygame.init()
resolution = (1280, 720)
screen = pygame.display.set_mode(resolution)
running = True
clock = pygame.time.Clock()
camera = gameplay.Camera()
player = gameplay.Player()

program_manifest = json.load(open("assets/manifest.json"))
pygame.display.set_caption(program_manifest["name"])
pygame.display.set_icon(pygame.image.load(program_manifest["icon"]))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)
    player.tick(0, camera)
    render.render_game(screen, 0, camera, resolution, player)
