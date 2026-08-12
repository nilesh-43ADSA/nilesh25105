class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def search(node, key):
    if node is None:
        return False
    if node.key == key:
        return True
    return search(node.left, key) or search(node.right, key)
def search_bst(node, key):
    if node is None:
        return False
    if node.key == key:
        return True
    if key < node.key:
        return search_bst(node.left, key)
    return search_bst(node.right, key)
root = Node(70)
root.left = Node(50)
root.right = Node(100)
root.left.left = Node(40)
root.left.right = Node(20)
print("Your Logic (Target 40):", search(root, 40))   
print("Optimized BST (Target 40):", search_bst(root, 40)) 
print("Your Logic (Target 90):", search(root, 90))      
print("Optimized BST (Target 90):", search_bst(root, 90))
