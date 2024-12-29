import pygame
import mathoperations
import json
import collision

player_sprite = pygame.image.load("assets/player.png")

class Player:
    def __init__(self, size: pygame.Vector2):
        self.position = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)
        self.size = size
        self.is_on_ground = False
    def tick(self, level_path: str):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.is_on_ground:
            self.velocity.y = -15
        if keys[pygame.K_LEFT]:
            self.velocity.x -= 2
        if keys[pygame.K_RIGHT]:
            self.velocity.x += 2
        self.velocity.x *= 0.8
        self.velocity += pygame.Vector2(0, 0.6)
        self.move(level_path)

    def draw(self, surface: pygame.surface, camera_pos: pygame.Vector2, resolution: tuple[int, int]):
        # pygame.draw.rect(surface, (30, 40, 230), (((self.position.x - (self.size.x / 2)) - camera_pos.x) + resolution[0] / 2, ((self.position.y - (self.size.y / 2)) - camera_pos.y) + resolution[1] / 2, self.size.x, self.size.y))
        surface.blit(player_sprite, (((self.position.x - (self.size.x / 2)) - camera_pos.x) + resolution[0] / 2, ((self.position.y - (self.size.y / 2)) - camera_pos.y) + resolution[1] / 2))
    def move(self, level_path: str):
        level = json.load(open(level_path))
        self.position.x += self.velocity.x
        for i in level:
            if i["type"] == 0:
               if collision.boxtobox((self.position.x, self.position.y, self.size.x, self.size.y), (i["position_x"], i["position_y"], i["width"], i["height"])):
                  if self.velocity.x > 0:
                      self.position.x = (i["position_x"] - ((self.size.x + i["width"]) / 2)) # - 1 # Ingore random +/- 1, just an old problem with collision detection (Now fixed)
                      self.velocity.x = 0
                  if self.velocity.x < 0:
                     self.position.x = (i["position_x"] + ((self.size.x + i["width"]) / 2)) # + 1
                     self.velocity.x = 0
        self.position.y += self.velocity.y
        self.is_on_ground = False
        for i in level:
            if collision.boxtobox((self.position.x, self.position.y, self.size.x, self.size.y), (i["position_x"], i["position_y"], i["width"], i["height"])):
                if self.velocity.y > 0:
                    self.position.y = (i["position_y"] - ((self.size.y + i["height"]) / 2)) # - 1
                    self.is_on_ground = True
                    self.velocity.y = 0
                if self.velocity.y < 0:
                    self.position.y = (i["position_y"] + ((self.size.y + i["height"]) / 2)) # + 1
                    self.velocity.y = 0