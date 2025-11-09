import heapq
from typing import Dict, List, Tuple, Any
import networkx as nx
import matplotlib.pyplot as plt
INF = float('inf')
def dijkstra(graph: Dict[Any, List[Tuple[Any, float]]], source: Any):
    dist = {node: INF for node in graph}
    parent = {node: None for node in graph}
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, u = heapq.heappop(heap)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(heap, (nd, v))
    return dist, parent
def reconstruct_path(parent: Dict[Any, Any], source: Any, target: Any) -> List[Any]:
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        if cur == source:
            break
        cur = parent[cur]
    path.reverse()
    return path
def draw_graph(graph, path=None):
    G = nx.DiGraph()
    # Add edges with weights
    for u in graph:
        for v, w in graph[u]:
            G.add_edge(u, v, weight=w)
    pos = nx.spring_layout(G, seed=42)  # layout for positioning
    # Draw nodes and edges
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, arrowsize=20)
    # Draw edge weights
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    # Highlight shortest path
    if path and len(path) > 1:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=3)
    plt.title("Graph with Shortest Path Highlighted")
    plt.show()
if __name__ == "__main__":
    graph = {
        'A': [('B', 2), ('C', 5)],
        'B': [('C', 1), ('D', 4)],
        'C': [('D', 1)],
        'D': [('E', 3)],
        'E': []
    }
    src = 'A'
    target = 'E'
    dist, parent = dijkstra(graph, src)
    path = reconstruct_path(parent, src, target)
    print("Shortest distances from", src)
    for node in sorted(graph):
        print(f"  {node}: {dist[node]}")
    if path:
        print(f"\nShortest path {src} -> {target}: {' -> '.join(path)} (cost {dist[target]})")
    else:
        print(f"No path from {src} to {target}")
    # Draw the graph and highlight shortest path
    draw_graph(graph, path)



