import pygame as pg
import math
from configuracion import *

class RayCasting: #Clase principal
    def __init__(self, game):
        self.game = game #Se crea una variable para el juego

    def ray_cast(self):
        ox, oy = self.game.jugador.pos
        x_map, y_map = self.game.jugador.map_pos

        ray_angle = self.game.jugador.angle - Confi.HALF_FOV + 0.0001
        for i in range(0,800):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # horizontals
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(0,20):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.mapa.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # verticals
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(0,20):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.mapa.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # depth
            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor

            #Digujar
            pg.draw.line(self.game.screen, 'yellow', (100 * ox, oy * 100),
                          (100 * ox + 100 * depth * cos_a, 100 * oy + 100 * depth * sin_a), 2)

            ray_angle += Confi.DELTA_ANGLE
    def update(self):
        pass
    
    

    