import pygame as pg
from configuracion import *


class ObjetoRender:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_texture = pg.image.load('texturas/wall.jpg')

    def obtenerTextura(path, res =(Confi.texturaEspacio, Confi.texturaEspacio)):
        textura = pg.image.load(path).convert_alpha() #carga la textura
        return pg.transform.scale(textura, res)
    
    def load_wall_texture(self):
        return {
            1: self.obtenerTextura('recursos/texturas/1.jpg'),
            2: self.obtenerTextura('recursos/texturas/2.jpg'),
            3: self.obtenerTextura('recursos/texturas/3.jpg'),
            4: self.obtenerTextura('recursos/texturas/4.jpg'),
            5: self.obtenerTextura('recursos/texturas/5.jpg'),
        }