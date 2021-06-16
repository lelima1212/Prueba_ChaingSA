from collections import deque
import sys


def busqueda_usuario(grafo, user1, user2):
    cola = deque([user1])
    nivel = {user1: 0}
    nodo_padre = {user1: None}
    i = 1
    while cola:
        vertice = cola.popleft()
        for neighbor in graph[vertice]:
            if neighbor not in nivel:
                cola.append(neighbor)
                nivel[neighbor] = i
                nodo_padre[neighbor] = vertice
        i = i + 1
        if nivel.get(user2):
            return nivel, nodo_padre
    return nivel, nodo_padre


def distancia_usuario(user1, user2):
    grafo = dict()
    //Se supone que el grafo esta lleno
    resultado = busqueda_usuario(grafo, user1, user2)
    print("La distancia  es %i" % (resultado[0][user2]))

