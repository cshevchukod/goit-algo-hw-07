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


def sum_values(root):

    if root is None:
        return 0
    return root.key + sum_values(root.left) + sum_values(root.right)


if __name__ == "__main__":
    root = None
    keys = [7, 3, 9, 1, 5, 8, 10, 2]

    for key in keys:
        root = insert(root, key)

    print(root)
    print("Sum =", sum_values(root))  # очікувано 45
