/// Sorts the given array, in place, by using the Insertion sort algorithm.
pub fn sort_by_bubble_sort(array: &mut [usize]) {
    let mut done = false;

    while !done {
        done = true;

        for index in 0..array.len() - 1 {
            if array[index] > array[index + 1] {
                done = false;

                array.swap(index, index + 1)
            }
        }
    }
}