class BinarySearchTree():
    def __init__(self, value, sx=None, dx=None):
        self.value = value
        self.sx = sx
        self.dx = dx

    def from_list(array):
        bst = BinarySearchTree(array[0])

        for i in range(1, len(array)):
            BinarySearchTree.insert(bst, array[i])

        return bst

    def show_in_order(bst):
        if bst.sx:
            BinarySearchTree.show_in_order(bst.sx)

        print(bst.value, end=" ")

        if bst.dx:
            BinarySearchTree.show_in_order(bst.dx)

    def insert(bst, element):
        if bst.value > element:
            if bst.sx:
                BinarySearchTree.insert(bst.sx, element)
            else:
                bst.sx = BinarySearchTree(element)
        elif bst.value < element:
            if bst.dx:
                BinarySearchTree.insert(bst.dx, element)
            else:
                bst.dx = BinarySearchTree(element)
        else:
            raise ValueError("The value is already in the Binary Search Tree.")

    def binary_search(bst, target):
        output = None

        if bst.value > target:
            if bst.sx:
                output = BinarySearchTree.binary_search(bst.sx, target)
        elif bst.value < target:
            if bst.dx:
                output = BinarySearchTree.binary_search(bst.dx, target)
        else:
            output = bst

        return output

def binary_search_iterative(array, target):
    start = 0
    end = len(array) - 1

    half = (start + end) // 2

    while array[half] != target:
        if array[half] < target:
            start = half + 1
        else:
            end = half - 1

        if start > end:
            return -1

        half = (start + end) // 2

    return half

def binary_search(array, target, start, end):
    if start > end:
        return -1

    half = (start + end) // 2

    if array[half] == target:
        return half

    if array[half] < target:
        return binary_search(array, target, half + 1, end)
    else:
        return binary_search(array, target, start, half - 1)

def binary_search_recursive(array, target):
    return binary_search(array, target, 0, len(array) - 1)