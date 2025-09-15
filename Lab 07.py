# Implement Binary Tree


# Implementing a binary tree involves two main steps:

# Node Class

class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

#  Building the Tree
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)

# In-order Traversal (Left -> Root -> Right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

inorder(root)
print(inorder(root))


# Pre-order Traversal (Root -> Left -> Right)

def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)

preorder(root)
print(preorder(root))



# Post-order Traversal (Left -> Right -> Root)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")

postorder(root)
print(postorder(root))



