use std::collections::HashMap;

struct Solution {}
impl Solution {
    pub fn equal_pairs(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut answer = 0;

        // Create a hash map
        let mut hash_map: HashMap<Vec<i32>, i32> = HashMap::with_capacity(n);
        for col in 0..n {
            let line: Vec<i32> = (0..n).map(|row| grid[row][col]).collect();
            if let Some(v) = hash_map.get_mut(&line) {
                *v += 1;
            } else {
                hash_map.insert(line, 1);
            }
        }

        // Search each key
        let answer = grid
            .iter()
            .fold(0, |a, line| a + hash_map.get(line).unwrap_or(&0));

        answer
    }
}
