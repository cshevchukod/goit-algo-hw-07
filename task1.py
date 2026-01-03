class BinaryTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(root, key):

    if root is None:
        return BinaryTreeNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def find_max(root):

    if root is None:
        return None
    
    current = root
    while current.right is not None:
        current = current.right

    return current.key


if __name__ == "__main__":
    root = None
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for key in keys:
        root = insert(root, key)

    print(root)
    print("Max =", find_max(root))
