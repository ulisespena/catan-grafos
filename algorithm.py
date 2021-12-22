import pcst_fast
import networkx as nx
from itertools import combinations

def calc_best_positions(prizes):
    edges = [
        [0,   3], [0,   4], #  0
        [1,   4], [1,   5], #  1
        [2,   5], [2,   6], #  2
        [3,   7],           #  3
        [4,   8],           #  4
        [5,   9],           #  5
        [6,  10],           #  6
        [7,  11], [7,  12], #  7
        [8,  12], [8,  13], #  8
        [9,  13], [9,  14], #  9
        [10, 14], [10, 15], # 10
        [11, 16],           # 11
        [12, 17],           # 12
        [13, 18],           # 13
        [14, 19],           # 14
        [15, 20],           # 15
        [16, 21], [16, 22], # 16
        [17, 22], [17, 23], # 17
        [18, 23], [18, 24], # 18
        [19, 24], [19, 25], # 19
        [20, 25], [20, 26], # 20
        [21, 27],           # 21
        [22, 28],           # 22
        [23, 29],           # 23
        [24, 30],           # 24
        [25, 31],           # 25
        [26, 32],           # 26
        [27, 33],           # 27
        [28, 33], [28, 34], # 28
        [29, 34], [29, 35], # 29
        [30, 35], [30, 36], # 30
        [31, 36], [31, 37], # 31
        [32, 37],           # 32
        [33, 38],           # 33
        [34, 39],           # 34
        [35, 40],           # 35
        [36, 41],           # 36
        [37, 42],           # 37
        [38, 43],           # 38
        [39, 43], [39, 44], # 39
        [40, 44], [40, 45], # 40
        [41, 45], [41, 46], # 41
        [42, 46],           # 42
        [43, 47],           # 43
        [44, 48],           # 44
        [45, 49],           # 45
        [46, 50],           # 46
        [47, 51],           # 47
        [48, 51], [48, 52], # 48
        [49, 52], [49, 53], # 49
        [50, 53],           # 50
    ]

    cost = 0
    while True:
        costs = [cost] * 72
        result_nodes, result_edges = pcst_fast.pcst_fast(edges, prizes, costs, -1, 1, 'gw', 0)
        if len(result_nodes) <= 16:
            break
        cost += 0.1

    n = len(result_nodes)

    # key: índice en grafo original => value: índice en nuevo subgrafo de NetworkX
    new_indexes = {}

    new_edges = {}
    for i, index in enumerate(result_edges):
        new_edges[index] = i

    subgraph_prizes = []
    for i, index in enumerate(result_nodes):
        subgraph_prizes.append(prizes[index])
        new_indexes[index] = i

    # corregir aristas no consideradas por PCST
    subgraph_edges = []
    for comb in combinations(result_nodes, 2):
        for edge in edges:
            if sorted(comb) == sorted(edge):
                # buscamos en las aristas originales si estas deben estar unidas
                # pero obtenemos los índices relativos al nuevo subgrafo
                subgraph_edges.append(sorted((new_indexes[comb[0]], new_indexes[comb[1]])))

    # calculamos el grafo complementario
    # con n: cantidad de nodos de subgrafo entregado
    # por PCST
    inverse_edges = []
    for comb in combinations(range(n), 2):
        comb = sorted(comb)
        if comb in subgraph_edges \
        or comb in inverse_edges:
            continue

        inverse_edges.append(comb)

    # creamos el grafo en NetworkX
    G = nx.Graph()
    G.add_nodes_from(subgraph_prizes)
    G.add_edges_from(inverse_edges)

    # obtenemos todos los cliques
    # y seleccionamos solamente los largo 5
    cliques = nx.enumerate_all_cliques(G)
    cliques_5 = [clique for clique in cliques if len(clique) == 5]

    # iteramos todos los cliques seleccionados
    # guardando el que presenta mayor valor total
    max_prize = 0
    max_clique = None
    for clique in cliques_5:
        prize = 0
        for node_index in clique:
            prize += subgraph_prizes[node_index]
        if prize > max_prize:
            max_prize = prize
            max_clique = clique

    # falta determinar las aristas del clique solución
    subgraph_edges = [[new_indexes[edges[edge][0]], new_indexes[edges[edge][1]]] for edge in result_edges]
    subgraph_prizes = [1 if i in max_clique else 0 for i in range(len(result_nodes))]
    subgraph_costs = [0 for _ in range(len(subgraph_edges))]

    result_nodes, result_edges = pcst_fast.pcst_fast(subgraph_edges, subgraph_prizes, subgraph_costs, -1, 1, 'gw', 0)

    # pasamos indexes de subgrafo a indexes del grafo original
    # invertimos el diccionario new_indexes
    inv_indexes = {value: key for key, value in new_indexes.items()}
    max_clique_original = [inv_indexes[index] for index in max_clique]

    inv_edges = {value: key for key, value in new_edges.items()}
    edges_original = [inv_edges[index] for index in result_edges]

    return max_clique_original, edges_original