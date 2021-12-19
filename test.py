import pcst_fast
import networkx as nx
from itertools import combinations

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

# prizes = [
#           10, 6, 10,
#         10, 16, 16, 10,
#         13, 22, 24, 19,
#        3, 19, 20, 27, 9,
#       11, 13, 18, 27, 21,
#      8, 15, 14, 22, 33, 12,
#      8, 21, 8, 20, 24, 12,
#       17, 13, 10, 18, 14,
#         9, 19, 9, 10, 2,
#          19, 13, 11, 4,
#          10, 13, 5, 2,
#             10, 3, 2
# ]

prizes = [
               0.278, 0.224, 0.278,
            0.278, 0.502, 0.502, 0.278,
            0.390, 0.668, 0.780, 0.610,
        0.112, 0.556, 0.668, 0.888, 0.332,
        0.334, 0.389, 0.556, 1.166, 0.776,
     0.222, 0.445, 0.389, 0.946, 1.332, 0.444,
     0.222, 0.665, 0.223, 0.892, 1.056, 0.444,
        0.554, 0.443, 0.336, 1.036, 0.500,
        0.332, 0.610, 0.307, 0.336, 0.056,
            0.610, 0.361, 0.363, 0.112,
            0.278, 0.361, 0.139, 0.056,
               0.278, 0.083, 0.056
]

cost = 0
while True:
    costs = [cost] * 72
    result_nodes, result_edges = pcst_fast.pcst_fast(edges, prizes, costs, -1, 1, 'gw', 0)
    if len(result_nodes) <= 16:
        break
    cost += 0.1

n = len(result_nodes)

new_indexes = {}
subgraph_prizes = []
for i, index in enumerate(result_nodes):
    subgraph_prizes.append(prizes[index])
    new_indexes[index] = i

# corregir aristas no consideradas por PCST
subgraph_edges = []
for comb in combinations(result_nodes, 2):
    for edge in edges:
        if comb == (edge[0], edge[1]) or comb == (edge[1], edge[0]):
            subgraph_edges.append((new_indexes[comb[0]], new_indexes[comb[1]]))

print(result_nodes)
print(subgraph_edges)

inverse_edges = []
for i in range(n):
    for j in range(n):
        if i == j \
            or (i, j) in subgraph_edges \
            or (j, i) in subgraph_edges \
            or (i, j) in inverse_edges \
            or (j, i) in inverse_edges:
            continue

        inverse_edges.append((i, j))

G = nx.Graph()
G.add_nodes_from(subgraph_prizes)
G.add_edges_from(inverse_edges)

cliques = nx.enumerate_all_cliques(G)
cliques_5 = [clique for clique in cliques if len(clique) == 5]

max_prize = 0
max_clique = None
for clique in cliques_5:
    prize = 0
    for node_index in clique:
        prize += subgraph_prizes[node_index]
    if prize > max_prize:
        max_prize = prize
        max_clique = clique

print(max_clique, max_prize)

# max_clique = nx.max_weight_clique(G, weight=None)
# for node_index in max_clique[0]:
#     print(node_index, subgraph_prizes[node_index])
