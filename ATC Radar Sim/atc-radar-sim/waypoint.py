import pygame as PG
import math as MATH

from config import (
    WAYPOINT_SIZE,
)

PG.init()
font = PG.font.Font(None, 18)

class Waypoint:
    def __init__(self, name: str, x: float, y: float) -> None:
        self.name = name
        self.x = x
        self.y = y
    
    def draw(self, screen: PG.Surface) -> None:
        p1 = (self.x, self.y - WAYPOINT_SIZE)
        p2 = (self.x - WAYPOINT_SIZE / 2, self.y + WAYPOINT_SIZE / 2)
        p3 = (self.x + WAYPOINT_SIZE / 2, self.y + WAYPOINT_SIZE / 2)
        PG.draw.polygon(screen, (0, 255, 255), [p1, p2, p3])
        text_surface = font.render(self.name, True, (0, 255, 255))
        text_rect = text_surface.get_rect(center = (self.x, self.y - 30))
        screen.blit(text_surface, text_rect)
        
    def is_clicked(self, mouse_pos):
        distance = MATH.sqrt((mouse_pos[0] - self.x) ** 2 + (mouse_pos[1] - self.y) ** 2)
        return distance <= 20