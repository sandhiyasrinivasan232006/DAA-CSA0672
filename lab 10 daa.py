from itertools import product
def dice_possibilities(n):
    total_possibilities= 6**n
    outcomes=list(product(range(1,7),repeat= n))
    return total_possibilities,outcomes
n = 2
total_possibilities,outcomes= dice_possibilities(n)
print(f"The total possibilities:{total_possibilities}")
print(f"All possibilities outcomes(total{len(outcomes)}):")
for outcomes in outcomes:
    print(outcomes)



from itertools import permutations
def traveling_salesperson_brute_force(graph, start):
    min_cost = float('inf')
    min_path = None
    for path in permutations(graph.keys()):
        if path[0] != start:
            continue
        cost = 0
        for i in range(len(path) - 1):
            if path[i + 1] not in graph[path[i]]:
                break
            cost += graph[path[i]][path[i + 1]]
        if cost < min_cost:
            min_cost = cost
            min_path = path
    return min_path, min_cost
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}
start_node = 'A'
best_path, min_distance = traveling_salesperson_brute_force(graph, start_node)
print(f"Best Path: {best_path}, Min Distance: {min_distance}")


def optimal_bst(keys, freq):
    n = len(keys)
    cost = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        cost[i][i] = freq[i]
    
    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i + L - 1
            cost[i][j] = float('inf')
            
            for r in range(i, j+1):
                c = sum(freq[i:j+1]) + (cost[i][r-1] if r > i else 0) + (cost[r+1][j] if r < j else 0)
                if c < cost[i][j]:
                    cost[i][j] = c
    
    return cost[0][n-1]

keys = [10, 12, 20]
freq = [34, 8, 50]
print(optimal_bst(keys, freq))
