def bfs_without(graph, start):
    visited = set()
    queue = [start]
    while queue:
        current = queue.pop(0)
        if current not in visited:
            print(current)
            visited.add(current)
            queue.extend(neighbor for neighbor in graph[current] if neighbor not in visited)
graph = {
    '0': ['1', '2'],
    '1': ['3', '4'],
    '2': ['5'],
    '3': [],
    '4': ['5'],
    '5': []
}
print("BFS without using deque:")
bfs_without(graph, '0')
from collections import deque
class GraphNode:
    def __init__(self, value):
        self.value = value
        self.adjacents = []
    def add_adjacent(self, adjacent):
        self.adjacents.append(adjacent)
def bfs_with_deque(start_node):
    visited = set()
    queue = deque([start_node])
    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            print(current_node.value)
            visited.add(current_node)
            for adjacent in current_node.adjacents:
                if adjacent not in visited:
                    queue.append(adjacent)
a = GraphNode('A')
b = GraphNode('B')
c = GraphNode('C')
d = GraphNode('D')
e = GraphNode('E')
a.add_adjacent(b)
a.add_adjacent(c)
b.add_adjacent(d)
b.add_adjacent(e)
c.add_adjacent(e)
print("\nBFS using deque:")
bfs_with_deque(a)
