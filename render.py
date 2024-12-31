import pygame
import json
import os; os.chdir(os.path.dirname(__file__))

texture_file = json.load(open("assets/textures.json"))
texture_list = []

for i in texture_file:
    texture_list.append(pygame.image.load(i["file"]))

level_file = json.load(open("assets/levels.json"))
level_list = []

for i in level_file:
    level_list.append(json.load(open(i["level_path"])))

def render_level(surface: pygame.surface, level_id: int, camera_position: pygame.Vector2, resolution: tuple[int, int]):
    file = level_list[level_id]
    for i in file:
         if i["type"] == 0:
             if i["texture"] == "none":
                 pygame.draw.rect(surface, (255, 255, 255), (((i["position_x"] - (i["width"] / 2)) - camera_position.x) + resolution[0] / 2, ((i["position_y"] - (i["height"] / 2)) - camera_position.y) + resolution[1] / 2, i["width"], i["height"]))
             else:
                 texture = texture_list[i["texture"]]
                 surface.blit(pygame.transform.scale(texture, (i["width"], i["height"])), (((i["position_x"] - (i["width"] / 2)) - camera_position.x) + resolution[0] / 2, ((i["position_y"] - (i["height"] / 2)) - camera_position.y) + resolution[1] / 2))
            # Make objects only draw when onscreen (Using the boxtobox function in collision.py)