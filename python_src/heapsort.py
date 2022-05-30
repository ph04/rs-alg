def build_max_heap(array, heap_size):
    for i in range(len(array) // 2, 0, -1):
        max_heapify(array, i, heap_size)

def get_left_child_index(index):
    return 2 * index

def get_right_child_index(index):
    return 2 * index + 1

def max_heapify(array, index, heap_size):
    array_len = len(array)

    curr_node = array[index - 1]

    left_child_index = get_left_child_index(index)
    right_child_index = get_right_child_index(index)

    if left_child_index <= array_len and right_child_index <= array_len:
        left_child = array[left_child_index - 1]
        right_child = array[right_child_index - 1]

        max_index = left_child_index if left_child_index <= heap_size and left_child > curr_node else index

        max_index = right_child_index if right_child_index <= heap_size and right_child > array[max_index - 1] else max_index

        if max_index != index:
            array[index - 1], array[max_index - 1] = array[max_index - 1], array[index - 1]

            max_heapify(array, max_index, heap_size)
    elif left_child_index <= array_len:
        left_child = array[left_child_index - 1]

        if left_child_index <= heap_size and left_child > curr_node:
            array[index - 1], array[left_child_index - 1] = array[left_child_index - 1], array[index - 1]

            max_heapify(array, left_child_index, heap_size)
    elif right_child_index <= array_len:
        right_child = array[right_child_index - 1]

        if right_child_index <= heap_size and right_child > curr_node:
            array[index - 1], array[right_child_index - 1] = array[right_child_index - 1], array[index - 1]

            max_heapify(array, right_child_index, heap_size)

def sort_by_heapsort(array):
    heap_size = len(array)

    build_max_heap(array, heap_size)

    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]

        heap_size -= 1

        max_heapify(array, 1, heap_size)