import pygame
import json
import os; os.chdir(os.path.dirname(__file__))
import gameplay
pygame.font.init()

texture_file = json.load(open("assets/textures.json"))
texture_list = []

for i in texture_file:
    texture_list.append(pygame.image.load(i["file"]))

level_file = json.load(open("assets/levels.json"))
level_list = []

for i in level_file:
    level_list.append(json.load(open(i["level_path"])))
    print("Render.py: " + i["level_name"] + " successfully loaded")


def render_game(surface: pygame.surface, level_id: int, camera: gameplay.Camera, resolution: tuple[int, int], player: gameplay.Player):
    file = level_list[level_id]
    surface.fill(((level_file[level_id])["background_color"]))
    for i in file:
         if i["type"] == 0:
             if i["texture"] == "none":
                 pygame.draw.rect(surface, (255, 255, 255), ((((i["position_x"] - (i["width"] / 2)) - camera.position.x) * camera.zoom) + resolution[0] / 2, (((i["position_y"] - (i["height"] / 2)) - camera.position.y) * camera.zoom) + resolution[1] / 2, i["width"] * camera.zoom, i["height"] * camera.zoom))
             else:
                 texture = texture_list[i["texture"]]
                 surface.blit(pygame.transform.scale(texture, (i["width"] * camera.zoom, i["height"] * camera.zoom)), (((i["position_x"] - (i["width"] / 2)) - camera.position.x) * camera.zoom + resolution[0] / 2, ((i["position_y"] - (i["height"] / 2)) - camera.position.y) * camera.zoom + resolution[1] / 2))
            # Make objects only draw when onscreen (Using the boxtobox() function in collision.py)
    player.draw(surface, camera, resolution)
    pygame.display.flip()