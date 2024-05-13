from collections import deque
from functools import lru_cache

'''
El siguiente código es una implementación de un algoritmo 
de búsqueda en anchura (BFS) para encontrar el camino más 
corto entre los NPC y el jugador.
'''

class PathFinding: 
    def __init__(self, game):
        self.game = game
        self.map = game.map.mini_map
        self.ways = [-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1]
        self.graph = {}
        self.get_graph()

    @lru_cache 
    def get_path(self, start, goal): #Obtenemos el camino entre dos puntos
        self.visited = self.bfs(start, goal, self.graph)
        path = [goal]
        step = self.visited.get(goal, start)

        while step and step != start:
            path.append(step)
            step = self.visited[step]
        return path[-1]

    def bfs(self, start, goal, graph): #Busqueda en anchura
        queue = deque([start]) #Cola de nodos a visitar
        visited = {start: None} #Diccionario de nodos visitados

        while queue: #Mientras haya nodos en la cola
            cur_node = queue.popleft() #Sacamos el primer nodo de la cola
            if cur_node == goal: #Si el nodo es el objetivo,
                break
            next_nodes = graph[cur_node] #Obtenemos los nodos adyacentes

            for next_node in next_nodes: #Recorremos los nodos adyacentes
                if next_node not in visited and next_node not in self.game.object_handler.npc_positions:
                    queue.append(next_node) 
                    visited[next_node] = cur_node #Añadimos el nodo a la cola
        return visited

    def get_next_nodes(self, x, y): #Funcion que obtiene los nodos adyacentes
        return [(x + dx, y + dy) for dx, dy in self.ways if (x + dx, y + dy) not in self.game.map.world_map]

    def get_graph(self): #Funcion que obtiene el grafo
        for y, row in enumerate(self.map): #Recorremos el mapa
            for x, col in enumerate(row):  
                if not col:
                    self.graph[(x, y)] = self.graph.get((x, y), []) + self.get_next_nodes(x, y) #Obtenemos los nodos adyacentes