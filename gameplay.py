import pygame
import mathoperations
import json
import collision

class Player:
    def __init__(self, size: pygame.Vector2):
        self.position = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)
        self.size = size
    def tick(self, level_path: str):
        level = open(level_path)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity -= pygame.Vector2(5, 0)
        self.velocity += pygame.Vector2(0, 0.6)
        self.position += self.velocity
        for i in json.load(level):
            if collision.boxtobox((self.position.x, self.position.y, self.size.x, self.size.y), (i["position_x"], i["position_y"], i["width"], i["height"])):
                self.position -= self.velocity
                self.velocity = pygame.Vector2(self.velocity.x, 0)

    def draw(self, surface: pygame.surface, camera_pos: pygame.Vector2, resolution: tuple[int, int]):
        pygame.draw.rect(surface, "blue", (((self.position.x - (self.size.x / 2)) - camera_pos.x) + resolution[0] / 2, ((self.position.y - (self.size.y / 2)) - camera_pos.y) + resolution[1] / 2, self.size.x, self.size.y))
