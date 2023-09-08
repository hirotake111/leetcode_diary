impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        use std::iter::once;
        let mut triangle = vec![vec![1]];
        for _ in 1..num_rows {
            let prev = triangle.last().unwrap();
            let new_one = prev.windows(2).map(|x| x[0] + x[1]);
            triangle.push(once(1).chain(new_one).chain(once(1)).collect());
        }

        triangle
    }
}
