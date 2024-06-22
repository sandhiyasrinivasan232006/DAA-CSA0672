def word_break(s,dict):
    n=len(s)
    dp=[False]*(n+1)
    dp[0]=True
    for i in range(1,n+1):
        for j in range(i):
            if dp[j]and s[j:i] in word_dict:
                dp[i]=True
                break
    return dp[n]
s="leetcode"
word_dict={"leet","code"}
print(word_break(s,word_dict))

def assembly_line_schedule(a, t, e, x, n):
    f1, f2 = e[0] + a[0][0], e[1] + a[1][0]
    for j in range(1, n):
        f1, f2 = min(f1 + a[0][j], f2 + t[1][j - 1] + a[0][j]), min(f2 + a[1][j], f1 + t[0][j - 1] + a[1][j])
    f_end = min(f1 + x[0], f2 + x[1])
    l_end = 1 if f_end == f1 + x[0] else 2
    return f_end, l_end
a = [[7, 9, 3, 4, 8, 4], [8, 5, 6, 4, 5, 7]]
t = [[2, 3, 1, 3, 4], [2, 1, 2, 2, 1]]
e = [2, 4]
x = [3, 2]
n = 6
f_end, l_end = assembly_line_schedule(a, t, e, x, n)
print("Fastest time:", f_end)
print("Line sequence:",l_end)

import heapq
from collections import defaultdict

# Prim's Algorithm
def prims_algorithm(graph):
    num_nodes = len(graph)
    mst_set = set()
    min_heap = [(0, 0)]  # (weight, node)
    total_weight = 0
    mst_edges = []

    while len(mst_set) < num_nodes:
        weight, node = heapq.heappop(min_heap)
        if node in mst_set:
            continue

        mst_set.add(node)
        total_weight += weight

        for adjacent, edge_weight in enumerate(graph[node]):
            if edge_weight > 0 and adjacent not in mst_set:
                heapq.heappush(min_heap, (edge_weight, adjacent))
                if weight > 0:
                    mst_edges.append((node, adjacent, edge_weight))

    return total_weight, mst_edges

# Kruskal's Algorithm
class UnionFind:
    def _init_(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskals_algorithm(num_nodes, edges):
    uf = UnionFind(num_nodes)
    mst_edges = []
    total_weight = 0

    edges.sort(key=lambda x: x[2])  # Sort edges by weight

    for node1, node2, weight in edges:
        if uf.find(node1) != uf.find(node2):
            uf.union(node1, node2)
            mst_edges.append((node1, node2, weight))
            total_weight += weight

    return total_weight, mst_edges

# Borůvka's Algorithm
def boruvkas_algorithm(num_nodes, edges):
    uf = unionfind(num_nodes)
    mst_edges = []
    total_weight = 0

    num_components = num_nodes

    while num_components > 1:
        cheapest = [-1] * num_nodes

        for node1, node2, weight in edges:
            root1 = uf.find(node1)
            root2 = uf.find(node2)

            if root1 != root2:
                if cheapest[root1] == -1 or cheapest[root1][2] > weight:
                    cheapest[root1] = (node1, node2, weight)
                if cheapest[root2] == -1 or cheapest[root2][2] > weight:
                    cheapest[root2] = (node1, node2, weight)

        for node in range(num_nodes):
            if cheapest[node] != -1:
                node1, node2, weight = cheapest[node]
                if uf.find(node1) != uf.find(node2):
                    uf.union(node1, node2)
                    mst_edges.append((node1, node2, weight))
                    total_weight += weight
                    num_components -= 1

    return total_weight, mst_edges

# Example usage
graph_adj_matrix = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

edges_list = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]

# Prim's Algorithm
total_weight_prims, mst_edges_prims = prims_algorithm(graph_adj_matrix)
print("Prim's Algorithm:")
print(f"Total weight of MST: {total_weight_prims}")
print("Edges in the MST:")
for edge in mst_edges_prims:
    print(edge)

# Kruskal's Algorithm
total_weight_kruskals, mst_edges_kruskals = kruskals_algorithm(len(graph_adj_matrix), edges_list)
print("\nKruskal's Algorithm:")
print(f"Total weight of MST: {total_weight_kruskals}")
print("Edges in the MST:")
for edge in mst_edges_kruskals:
    print(edge)

# Borůvka's Algorithm
total_weight_boruvkas, mst_edges_boruvkas = boruvkas_algorithm(len(graph_adj_matrix), edges_list)
print("\nBorůvka's Algorithm:")
print(f"Total weight of MST: {total_weight_boruvkas}")
print("Edges in the MST:")
for edge in mst_edges_boruvkas:
    print(edge)
