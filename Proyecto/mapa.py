import pygame as pg



_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 3, 3, 3, 3, _, _, _, 2, 2, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
    [1, _, _, 3, 3, 3, 3, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, 4, _, _, _, 4, _, _, _, _, _, _, 1],
    [1, 1, 1, 3, 1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1]

    
]

class Map:
    def __init__(self, game): #constructor de la clase
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.rows = len(self.mini_map) #numero de filas
        self.cols = len(self.mini_map[0]) #numero de columnas
        self.get_map() #obtiene el mapa

    def get_map(self):
        for j, row in enumerate(self.mini_map): #recorre las filas
            for i, value in enumerate(row): #recorre las columnas
                if value:
                    self.world_map[(i, j)] = value #guarda el valor en el mapa

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2) #dibuja el mapa
         for pos in self.world_map]