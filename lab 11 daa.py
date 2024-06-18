def assembly_line_scheduling(e1, e2, x1, x2, a1, a2, t1, t2, n):
    f1 = [0] * n
    f2 = [0] * n
    f1[0] = e1 + a1[0]
    f2[0] = e2 + a2[0]
    for i in range(1, n):
        f1[i] = min(f1[i - 1] + a1[i], f2[i - 1] + t2[i - 1] + a1[i])
        f2[i] = min(f2[i - 1] + a2[i], f1[i - 1] + t1[i - 1] + a2[i])
    return min(f1[n - 1] + x1, f2[n - 1] + x2)
e1 = 20
e2 = 4
x1 = 3
x2 = 2
a1 = [7, 9, 3, 4, 8]
a2 = [8, 5, 6, 4, 5]
t1 = [2, 3, 1, 3]
t2 = [2, 1, 2, 2]
n = 5 
print(assembly_line_scheduling(e1, e2, x1, x2, a1,a2,t1,t2,n))

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(knapsack(values, weights, capacity))


def flyod_warshall(graph):
    n=len(graph)
    dist=graph
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
    return dist
graph=[
    [0, float('inf'), 3, float('inf')],
    [2, 0, float('inf'), float('inf')],
    [float('inf'), 7, 0, 1],
    [6, float('inf'), float('inf'), 0]
]
result= flyod_warshall(graph)
for row in result:
    print(row)
