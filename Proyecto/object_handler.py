from sprite_object import *
from npc import *
from random import choices, randrange #


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = [] #Lista de sprites
        self.npc_list = [] #Lista de NPCs
        # Rutas de los sprites
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite #Añadimos un sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        # NPC generation
        self.enemies = 15  # Numero de NPCs
        self.npc_types = [SoldierNPC, CacoDemonNPC, CyberDemonNPC]
        self.weights = [70, 20, 10] 
        self.restricted_area = {(i, j) for i in range(10) for j in range(10)} #Area restringida
        self.spawn_npc() #Generamos los NPCs

        #  Posiciones de los sprites
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 3.25)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 4.75)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 2.5)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 5.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 4.5)))
        #  Posiciones de las lamparas
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 5.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(12.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(9.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 12.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(9.5, 20.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(10.5, 20.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(3.5, 14.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(3.5, 18.5)))
        #  Posiciones de las cajas
        add_sprite(AnimatedSprite(game, pos=(14.5, 24.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 30.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 30.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 24.5)))

        

    def spawn_npc(self):
        for i in range(self.enemies): #Generamos los NPCs
                npc = choices(self.npc_types, self.weights)[0] #Elegimos un NPC
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows) #Posicionamos el NPC
                while (pos in self.game.map.world_map) or (pos in self.restricted_area): #Comprobamos que la posicion no este ocupada
                    pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5))) 
 
    def check_win(self): #Comprobamos si el jugador ha ganado
        if not len(self.npc_positions): #Si no quedan NPCs
            self.game.object_renderer.win() #Mostramos el mensaje de victoria
            pg.display.flip()
            pg.time.delay(3500) #Esperamos 1.5 segundos
            self.game.new_game()

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive} #Posiciones de los NPCs
        [sprite.update() for sprite in self.sprite_list] #Actualizamos los sprites
        [npc.update() for npc in self.npc_list] #Actualizamos los NPCs
        self.check_win() 

    def add_npc(self, npc):
        self.npc_list.append(npc) #Añadimos un NPC

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite) #Añadimos un sprite