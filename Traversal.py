class Node:
    def __init__(self, key):
        self.left = self.right = None
        self.val = key

def insert(root, key):
    if not root: return Node(key)
    if key < root.val: root.left = insert(root.left, key)
    else: root.right = insert(root.right, key)
    return root

# Traversals (L = Left, R = Right, V = Value/Root)
def inorder(root):    # L -> V -> R
    if root: inorder(root.left); print(root.val, end=" "); inorder(root.right)

def preorder(root):   # V -> L -> R
    if root: print(root.val, end=" "); preorder(root.left); preorder(root.right)

def postorder(root):  # L -> R -> V
    if root: postorder(root.left); postorder(root.right); print(root.val, end=" ")

# Quick test
root = None
for x in [12,5,6,3,14,13]:
    root = insert(root, x)
print("Inorder: "); inorder(root)      # Output: 20 30 40 50 70
print("\nPreorder: "); preorder(root)   # Output: 50 30 20 40 70
print("\nPostorder: "); postorder(root) # Output: 20 40 30 70 50
