
# Import deque to create a queue for level-order traversal.
from collections import deque

# Define a class called Node to represent one node in our binary tree.
class Node:

    # This method runs automatically whenever we create a new Node.
    def __init__(self, value):

        # Store the value or number inside the node.
        self.value = value

        # Create an empty space for the left child of this node.
        self.left = None

        # Create an empty space for the right child of this node.
        self.right = None

# Define a function that builds the binary tree from the assignment.
def build_tree():

    # Create an empty dictionary to store all 31 tree nodes.
    nodes = {}

    # Create nodes numbered from 1 up to 31.
    for number in range(1, 32):

        # Create a Node object and store it using its number as the key.
        nodes[number] = Node(number)

    # Connect the parent nodes to their children.
    for number in range(1, 16):

        # Connect the left child using the formula: parent number multiplied by 2.
        nodes[number].left = nodes[number * 2]

        # Connect the right child using the formula: parent number multiplied by 2, plus 1.
        nodes[number].right = nodes[number * 2 + 1]

    # Return Node 1 because it is the root of the entire tree.
    return nodes[1]

# Define a function to perform pre-order traversal of the binary tree.
def preorder_traversal(root):

    # Check whether the current node is empty.
    if root is None:

        # Stop this recursive call if there is no node.
        return

    # Visit and display the current root node first.
    print(root.value, end=" ")

    # Recursively visit all nodes in the left subtree.
    preorder_traversal(root.left)

    # Recursively visit all nodes in the right subtree.
    preorder_traversal(root.right)


# Define a function to perform in-order traversal of the binary tree.
def inorder_traversal(root):

    # Check whether the current node is empty.
    if root is None:

        # Stop this recursive call if there is no node.
        return

    # Recursively visit all nodes in the left subtree first.
    inorder_traversal(root.left)

    # Visit and display the current root node.
    print(root.value, end=" ")

    # Recursively visit all nodes in the right subtree.
    inorder_traversal(root.right)


# Define a function to perform post-order traversal of the binary tree.
def postorder_traversal(root):

    # Check whether the current node is empty.
    if root is None:

        # Stop this recursive call if there is no node.
        return

    # Recursively visit all nodes in the left subtree first.
    postorder_traversal(root.left)

    # Recursively visit all nodes in the right subtree second.
    postorder_traversal(root.right)

    # Visit and display the current root node last.
    print(root.value, end=" ")


# Define a function to perform level-order traversal of the binary tree.
def levelorder_traversal(root):

    # Check whether the tree is empty.
    if root is None:

        # Stop the function if there is no root node.
        return

    # Create an empty queue to hold nodes waiting to be visited.
    queue = deque()

    # Add the root node to the queue first.
    queue.append(root)

    # Continue while there are nodes waiting in the queue.
    while queue:

        # Remove the first node from the front of the queue.
        current = queue.popleft()

        # Display the value of the node we just removed.
        print(current.value, end=" ")

        # Check whether the current node has a left child.
        if current.left is not None:

            # Add the left child to the end of the queue.
            queue.append(current.left)

        # Check whether the current node has a right child.
        if current.right is not None:

            # Add the right child to the end of the queue.
            queue.append(current.right)






# Run this section only when this Python file is executed directly.
if __name__ == "__main__":

    # Build the complete binary tree containing 31 nodes.
    root = build_tree()

    # Display the heading for the binary tree traversal results.
    print("\n========== BINARY TREE TRAVERSALS ==========")

    # Display the heading for the pre-order traversal.
    print("\n1. Pre-order Traversal:")

    # Perform the pre-order traversal of the tree.
    preorder_traversal(root)

    # Move to a new line after the pre-order results.
    print()

    # Display the heading for the in-order traversal.
    print("\n2. In-order Traversal:")

    # Perform the in-order traversal of the tree.
    inorder_traversal(root)

    # Move to a new line after the in-order results.
    print()

    # Display the heading for the post-order traversal.
    print("\n3. Post-order Traversal:")

    # Perform the post-order traversal of the tree.
    postorder_traversal(root)

    # Move to a new line after the post-order results.
    print()

    # Display the heading for the level-order traversal.
    print("\n4. Level-order Traversal:")

    # Perform the level-order traversal of the tree.
    levelorder_traversal(root)

    # Move to a new line after the level-order results.
    print()

    # Display a closing message after all traversals are complete.
    print("\n========== TRAVERSALS COMPLETED ==========")
