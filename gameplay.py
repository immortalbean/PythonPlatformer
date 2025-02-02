import pygame
import player
import mathoperations
import collision
import json

class Camera:
    def __init__(self):
        self.position: pygame.Vector2 = pygame.Vector2(0, 0)