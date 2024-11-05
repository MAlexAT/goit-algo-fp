import matplotlib.pyplot as plt
import networkx as nx
import uuid
from collections import deque

# Визначення класу вузла
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

# Додаємо ребра для графу
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Малювання дерева
def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    node_colors = [tree.nodes[node]['color'] for node in tree.nodes]
    labels = {node: tree.nodes[node]['label'] for node in tree.nodes}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, node_size=2000, node_color=node_colors, font_size=10)
    plt.show()

# Генерація яскравих кольорів
def generate_colors(steps):
    return [f"#{hex(255 - int(i * 255 / steps))[2:]:0>2}99FF" for i in range(steps)]

# Обхід в глибину (DFS) з візуалізацією
def dfs_visual(root):
    stack = [root]
    visited_colors = {}
    colors = generate_colors(20)  # генеруємо більше кольорів
    step = 0
    
    while stack:
        node = stack.pop()
        if node and node.id not in visited_colors:
            visited_colors[node.id] = colors[step]
            node.color = colors[step]
            step += 1
            stack.append(node.right)
            stack.append(node.left)
            draw_tree(root, colors)
    print("DFS обход завершено.")

# Обхід в ширину (BFS) з візуалізацією
def bfs_visual(root):
    queue = deque([root])
    visited_colors = {}
    colors = generate_colors(20)  # генеруємо більше кольорів
    step = 0
    
    while queue:
        node = queue.popleft()
        if node and node.id not in visited_colors:
            visited_colors[node.id] = colors[step]
            node.color = colors[step]
            step += 1
            queue.append(node.left)
            queue.append(node.right)
            draw_tree(root, colors)
    print("BFS обход завершено.")

# Створення дерева
root = Node(10)
root.left = Node(6)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(8)
root.right.left = Node(12)
root.right.right = Node(18)

# Запуск візуалізації
print("DFS Візуалізація")
dfs_visual(root)
print("BFS Візуалізація")
bfs_visual(root)
