import pygame
import json
import collision
import gameplay
import mathoperations

player_sprite = pygame.image.load("assets/player.png")

level_file = json.load(open("assets/levels.json"))
level_list = []

for i in level_file:
    level_list.append(json.load(open(i["level_path"])))
    print("Player.py: " + i["level_name"] + " succesfully loaded")

class Player:
    def __init__(self, size: pygame.Vector2 = pygame.Vector2(30, 50), acceleration: float = 2, air_acceleration: float = 1, deceleration: float = 0.8, air_deceleration: float = 0.9, jump_power: float = -15, gravity_power: float = 1.2, jump_gravity_power: float = 0.6):
        self.position = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)
        self.is_on_ground = False
        self.size = size
        self.acceleration = acceleration
        self.air_acceleration = air_acceleration
        self.deceleration = deceleration
        self.air_deceleration = air_deceleration
        self.jump_power = jump_power
        self.direction = 1
        self.gravity_power = gravity_power
        self.jump_gravity_power = jump_gravity_power
    def tick(self, level_id: int, camera: gameplay.Camera):
        keys = pygame.key.get_pressed()
        self.applied_gravity = self.gravity_power
        if keys[pygame.K_UP]:
            self.applied_gravity = self.jump_gravity_power
            if self.is_on_ground:
                self.velocity.y = self.jump_power
                self.is_on_ground = False
        if keys[pygame.K_LEFT]:
            self.direction = -1
            if self.is_on_ground:
                self.velocity.x -= self.acceleration
            else:
                self.velocity.x -= self.air_acceleration
        if keys[pygame.K_RIGHT]:
            self.direction = 1
            if self.is_on_ground:
                self.velocity.x += self.acceleration
            else:
                self.velocity.x += self.air_acceleration
        if self.is_on_ground:
           self.velocity.x *= self.deceleration
        else:
            self.velocity.x *= self.air_deceleration

        self.velocity += pygame.Vector2(0, self.applied_gravity)
        self.move(level_id)
        camera.position = pygame.Vector2(mathoperations.lerp(camera.position.x, self.position.x, 0.2), mathoperations.lerp(camera.position.y, self.position.y - 100, 0.05))

    def draw(self, surface: pygame.surface, camera: gameplay.Camera, resolution: tuple[int, int]):
        # pygame.draw.rect(surface, (30, 40, 230), (((self.position.x - (self.size.x / 2)) - camera_pos.x) + resolution[0] / 2, ((self.position.y - (self.size.y / 2)) - camera_pos.y) + resolution[1] / 2, self.size.x, self.size.y))
        surface.blit(pygame.transform.flip(player_sprite, self.direction == -1, False), (((self.position.x - (self.size.x / 2)) - camera.position.x) + resolution[0] / 2, ((self.position.y - (self.size.y / 2)) - camera.position.y) + resolution[1] / 2))
    def move(self, level_id: int):
        #Integrate delta-time in the near future
        #Perhaps add slope support in the future
        level = level_list[level_id]
        self.position.x += self.velocity.x
        for i in level:
            if i["type"] == 0:
               if collision.boxtobox((self.position.x, self.position.y, self.size.x, self.size.y), (i["position_x"], i["position_y"], i["width"], i["height"])):
                  if self.velocity.x > 0:
                      self.position.x = (i["position_x"] - ((self.size.x + i["width"]) / 2))
                      self.velocity.x = 0
                  if self.velocity.x < 0:
                     self.position.x = (i["position_x"] + ((self.size.x + i["width"]) / 2))
                     self.velocity.x = 0
        self.position.y += self.velocity.y
        self.is_on_ground = False
        for i in level:
            if i["type"] == 0:
                if collision.boxtobox((self.position.x, self.position.y, self.size.x, self.size.y), (i["position_x"], i["position_y"], i["width"], i["height"])):
                    if self.velocity.y > 0:
                        self.position.y = (i["position_y"] - ((self.size.y + i["height"]) / 2)) # - 1
                        self.is_on_ground = True
                        self.velocity.y = 0
                    if self.velocity.y < 0:
                        self.position.y = (i["position_y"] + ((self.size.y + i["height"]) / 2)) # + 1
                        self.velocity.y = 0
        for i in level:
            if i["type"] == 1:
                if collision.boxtobox((self.position.x, self.position.y, self.size.x, self.size.y), (i["position_x"], i["position_y"], i["width"], i["height"])):
                    self.die()
    def die(self):
        self.position = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)
        self.is_on_ground = False
        self.direction = 1