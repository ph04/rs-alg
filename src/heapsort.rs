// TODO: reindex everything

/// Builds a max-heap from the given array.
fn build_max_heap(array: &mut [usize], heap_size: usize) {
    (1..=array.len() / 2).rev().for_each(|index| max_heapify(array, index, heap_size));
}

/// Returns the index of the left child.
fn get_left_child_index(index: usize) -> usize {
    2 * index
}

/// Returns the index of the right child.
fn get_right_child_index(index: usize) -> usize {
    2 * index + 1
}

/// Assumes that the right and left subtree are
/// already sorted, and fixes the position of the
/// current root of the heap.
fn max_heapify(array: &mut [usize], index: usize, heap_size: usize) {
    let current_node = array[index - 1]; // should always exist

    let left_child_index = get_left_child_index(index);
    let right_child_index = get_right_child_index(index);

    match (array.get(left_child_index - 1), array.get(right_child_index - 1)) {
        (Some(left_child), Some(right_child)) => {
            let mut max_index = if left_child_index <= heap_size && left_child > right_child {
                left_child_index
            } else {
                index
            };

            if right_child_index <= heap_size && *right_child > array[max_index - 1] {
                max_index = right_child_index
            }

            if max_index != index {
                array.swap(index - 1, max_index - 1);

                max_heapify(array, max_index, heap_size);
            }
        },
        (Some(left_child), None) => {
            if *left_child > current_node && left_child_index <= heap_size {
                array.swap(index - 1, left_child_index - 1);

                max_heapify(array, left_child_index, heap_size);
            }
        },
        (None, Some(right_child)) => {
            if *right_child > current_node && right_child_index <= heap_size {
                array.swap(index - 1, right_child_index - 1);

                max_heapify(array, right_child_index, heap_size);
            }
        },
        (_, _) => {},
    }
}

/// Sorts the given array, in place, by using the Heapsort algorithm.
pub fn sort_by_heapsort(array: &mut [usize]) {
    let mut heap_size = array.len();

    build_max_heap(array, heap_size);

    (2..array.len()).rev().for_each(|index| {
        array.swap(index, 0);

        heap_size -= 1;

        max_heapify(array, 1, heap_size);
    });
}