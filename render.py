import pygame
import json
import os; os.chdir(os.path.dirname(__file__))

texture_list = json.load(open("assets/textures.json"))

def render_level(surface: pygame.surface, level_path: str, camera_position: pygame.Vector2, resolution: tuple[int, int]):
    file = json.load(open(level_path))

    for i in file:
         if i["type"] == 0:
             if i["texture"] == "none":
                 pygame.draw.rect(surface, (255, 255, 255), (((i["position_x"] - (i["width"] / 2)) - camera_position.x) + resolution[0] / 2, ((i["position_y"] - (i["height"] / 2)) - camera_position.y) + resolution[1] / 2, i["width"], i["height"]))
             else:
                 texture_id = texture_list[i["texture"]]
                 texture = pygame.image.load(texture_id["file"])
                 surface.blit(pygame.transform.scale(texture, (i["width"], i["height"])), (((i["position_x"] - (i["width"] / 2)) - camera_position.x) + resolution[0] / 2, ((i["position_y"] - (i["height"] / 2)) - camera_position.y) + resolution[1] / 2))
            # Make objects only draw when onscreen (Using the boxtobox function in collision.py)