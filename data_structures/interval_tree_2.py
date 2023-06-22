class TreeNode:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.right = None
        self.left = None
        self.parent = None

if __name__ == "__main__":
    arr = [0, 7, 5, 3, 1, 8, 6, 12, 3]
    # Każdy element tej tablicy będzie liściem drzewa
