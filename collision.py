import pygame
import mathoperations
import json


def boxtobox(box1: pygame.rect, box2: pygame.rect) -> bool:
    temp = True
    if (box1[0] + box1[2] / 2) < (box2[0] - (box2[2] - 1) / 2):
        temp = False
    if (box1[0] - box1[2] / 2) > (box2[0] + (box2[2] - 1) / 2):
        temp = False
    if (box1[1] + box1[3] / 2) < (box2[1] - (box2[3] - 1) / 2):
        temp = False
    if (box1[1] - box1[3] / 2) > (box2[1] + (box2[3] - 1) / 2):
        temp = False
    return temp
