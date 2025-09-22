# 1. Node Class Definition
# Defines the structure for each node in the binary tree.
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

# 2. Traversal Function Implementations

# In-order Traversal (Left, Root, Right)
def inorder_traversal(root):
    """Performs in-order traversal of the tree."""
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# Pre-order Traversal (Root, Left, Right)
def preorder_traversal(root):
    """Performs pre-order traversal of the tree."""
    if root:
        print(root.val, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Post-order Traversal (Left, Right, Root)
def postorder_traversal(root):
    """Performs post-order traversal of the tree."""
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=" ")

# 3. Driver Code to Test the Implementation

if __name__ == "__main__":
    # Create the sample binary tree
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Binary Tree Traversal:")

    print("\nIn-order traversal (Left, Root, Right):")
    inorder_traversal(root)
    print()

    print("\nPre-order traversal (Root, Left, Right):")
    preorder_traversal(root)
    print()

    print("\nPost-order traversal (Left, Right, Root):")
    postorder_traversal(root)
    print()

