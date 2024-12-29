import pygame
import json
import os; os.chdir(os.path.dirname(__file__))

def render_level(surface: pygame.surface, level_path: str, camera_position: pygame.Vector2, resolution: tuple[int, int]):
    file = json.load(open(level_path))
    for i in file:
         if i["type"] == 0:
            pygame.draw.rect(surface, (250, 250, 255), (((i["position_x"] - (i["width"] / 2)) - camera_position.x) + resolution[0] / 2, ((i["position_y"] - (i["height"] / 2)) - camera_position.y) + resolution[1] / 2, i["width"], i["height"]))