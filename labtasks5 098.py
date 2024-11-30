class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.left = None
        self.right = None
    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
def dfs_stack(start_node):
    visited = set()
    stack = [start_node]
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            print(current_node.value)
            visited.add(current_node)
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
a.add_neighbor(b)
a.add_neighbor(c)
b.add_neighbor(d)
c.add_neighbor(e)
d.add_neighbor(a)
e.add_neighbor(b)
print("DFS Traversal:")
dfs_stack(a)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)
def preorder(root):
    if root:
        print(root.value, end=' ')
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=' ')
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("\nInorder Traversal:")
inorder(root)
print("\nPreorder Traversal:")
preorder(root)
print("\nPostorder Traversal:")
postorder(root)
