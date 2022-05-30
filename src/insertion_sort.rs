fn shift_array(array: &mut [usize], start: usize, end: usize) {
    for i in (start..end).rev() {
        array.swap(i, i + 1);
    }
}

/// Sorts the given array, in place, by using the Insertion sort algorithm.
pub fn sort_by_insertion_sort(array: &mut [usize]) {
    unimplemented!();

    for index in 1..array.len() {
        println!("{:?}", array);

        let current_element = array[index];

        let mut i = index - 1;

        if array[i] < current_element {
            continue;
        }

        while i != 0 && array[i] > current_element {
            i -= 1;
        }

        println!("{}", i);

        shift_array(array, i, index);
    }
}