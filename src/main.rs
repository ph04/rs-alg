use alg::heapsort::sort_by_heapsort;

fn main() {
    let mut array = [3, 6, 0, 4, 24, 10, 7, 2, 3, 4, 7, 3, 1, 0];

    sort_by_heapsort(&mut array);

    println!("{:?}", array);
}