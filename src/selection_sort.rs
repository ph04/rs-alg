fn get_min_index(last_slice: &[usize]) -> usize {
    let mut min = last_slice[0];
    let mut min_index = 0;

    for (index, element) in last_slice.iter().enumerate() {
        if *element < min {
            min = *element;
            min_index = index;
        }
    }

    min_index
}

pub fn sort_by_selection_sort(array: &mut [usize]) {
    for index in 0..array.len() - 1 {
        let mut min_index = get_min_index(&array[index..]);

        min_index += index;

        array.swap(index, min_index);
    }
}