def is_safe(g, v, pos, path):
    if g[path[pos - 1]][v] == 0:
        return False
    for vertex in path:
        if vertex == v:
            return False
    return True

def hamiltonian_recur(g, path, pos):
    n = len(g)
    if pos == n:
        if g[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    for v in range(n):
        if is_safe(g, v, pos, path) == True:
            path[pos] = v
            if hamiltonian_recur(g, path, pos + 1) == True:
                return True
            path[pos] = -1
        
    return False

def hamiltonian_cycle(g):
    n = len(g)
    path = [-1] * n
    path[0] = 0

    if hamiltonian_recur(g, path, 1) == False:
        print("해밀토니안 사이클 없음")
        return False
    else:
        print("해밀토니안 사이클: ", path)
        return True

def find_all_hamiltonian_cycles(g):
    n = len(g)
    cycles = []

    def backtrack(path, pos):
        if pos == n:
            if g[path[pos - 1]][path[0]] == 1:
                cycles.append(path[:])
            return

        for v in range(n):
            if is_safe(g, v, pos, path):
                path[pos] = v
                backtrack(path, pos + 1)
                path[pos] = -1

    path = [-1] * n
    path[0] = 0
    backtrack(path, 1)

    return cycles

def calculate_cycle_weight(g, cycle):
    weight = 0
    n = len(cycle)
    for i in range(n):
        weight += g[cycle[i - 1]][cycle[i]]
    return weight

# Example usage
g1 = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
]

g2 = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
]

g3 = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1],
]

def find_minimum_weight_cycle(graph):
    all_cycles = find_all_hamiltonian_cycles(graph)
    min_weight = float('inf')
    min_cycle = None

    for cycle in all_cycles:
        weight = calculate_cycle_weight(graph, cycle)
        if weight < min_weight:
            min_weight = weight
            min_cycle = cycle

    return min_cycle

print("g1에서 가장 낮은 가중치를 갖는 해밀토니안 사이클:")
min_cycle_g1 = find_minimum_weight_cycle(g1)
print("해밀토니안 사이클:", min_cycle_g1)
print("가중치:", calculate_cycle_weight(g1, min_cycle_g1))

print("g2에서 가장 낮은 가중치를 갖는 해밀토니안 사이클:")
min_cycle_g2 = find_minimum_weight_cycle(g2)
print("해밀토니안 사이클:", min_cycle_g2)
print("가중치:", calculate_cycle_weight(g2, min_cycle_g2))

print("g3에서 가장 낮은 가중치를 갖는 해밀토니안 사이클:")
min_cycle_g3 = find_minimum_weight_cycle(g3)
print("해밀토니안 사이클:", min_cycle_g3)
print("가중치:", calculate_cycle_weight(g3, min_cycle_g3))