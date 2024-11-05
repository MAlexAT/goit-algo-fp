import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Функція для додавання ребра в граф
def add_edge(graph, u, v, weight):
    graph[u].append((v, weight))
    graph[v].append((u, weight))  # Якщо граф неорієнтований, додаємо ребро в обидва напрямки

# Реалізація алгоритму Дейкстри з використанням бінарної купи
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)
    shortest_paths = {start: None}  # Для відстеження шляхів

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_paths[neighbor] = current_vertex  # Відстежуємо шлях
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances, shortest_paths

# Створення графа
graph = {
    'A': [],
    'B': [],
    'C': [],
    'D': [],
    'E': [],
    'F': []
}

# Додаємо ребра до графа (наприклад, транспортна мережа)
add_edge(graph, 'A', 'B', 4)
add_edge(graph, 'A', 'C', 2)
add_edge(graph, 'B', 'C', 5)
add_edge(graph, 'B', 'D', 10)
add_edge(graph, 'C', 'E', 3)
add_edge(graph, 'E', 'D', 4)
add_edge(graph, 'D', 'F', 11)

# Вибираємо початкову вершину та запускаємо алгоритм Дейкстри
start_vertex = 'A'
shortest_distances, shortest_paths = dijkstra(graph, start_vertex)

# Візуалізація графа з використанням NetworkX
G = nx.Graph()

# Додаємо ребра з вагами до графа NetworkX
for u in graph:
    for v, weight in graph[u]:
        G.add_edge(u, v, weight=weight)

# Позиції вузлів для візуалізації
pos = nx.spring_layout(G)  # Можна також використовувати інші методи, наприклад, circular_layout

# Малюємо граф
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G[u][v]['weight'] for u, v in G.edges})

# Відображення найкоротшого шляху від початкової вершини до всіх інших вершин
for target, previous in shortest_paths.items():
    if previous is not None:  # Відобразимо тільки шлях від початкової вершини
        path_edges = [(previous, target)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color='red')

# Налаштування графіка
plt.title(f"Найкоротші шляхи від вершини {start_vertex}")
plt.show()

# Вивід результатів найкоротших шляхів
print(f"Найкоротші шляхи від вершини {start_vertex}:")
for vertex, distance in shortest_distances.items():
    print(f"Відстань до {vertex}: {distance}")
