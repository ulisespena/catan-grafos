import pcst_fast
from random import shuffle

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

prizes = [
          10, 6, 10,
        10, 16, 16, 10,
        13, 22, 24, 19,
       3, 19, 20, 27, 9,
      11, 13, 18, 27, 21,
     8, 15, 14, 22, 33, 12,
     8, 21, 8, 20, 24, 12,
      17, 13, 10, 18, 14,
        9, 19, 9, 10, 2,
         19, 13, 11, 4,
         10, 13, 5, 2,
            10, 3, 2
]

# avgs = []
# for edge in edges:
#     avg = abs(prizes[edge[0]] - prizes[edge[1]])
#     avgs.append(avg)

# # foo = sum(avgs) / len(avgs)
# avgs.sort()
# avgs = avgs[:31]
# foo = sum(avgs) / len(avgs)

# avg_node_value = sum(prizes) / len(prizes)
# cost_value = sum(avgs) / len(avgs)
# costs = [avg_node_value] * 72

# foo *= 21
# print(foo)
# costs = [foo] * 72
# result_nodes, result_edges = pcst_fast.pcst_fast(edges, prizes, costs, -1, 1, 'gw', 0)

bar = 1
while True:
    costs = [bar] * 72
    result_nodes, result_edges = pcst_fast.pcst_fast(edges, prizes, costs, -1, 1, 'gw', 0)
    if len(result_nodes) <= 15:
        # print(bar)
        break
    bar += 1

print(len(result_nodes))
print(result_nodes)
print(result_edges)
