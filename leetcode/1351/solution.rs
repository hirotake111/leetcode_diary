impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let only_negative = |n: &&i32| n < &&0;
        let count_negative = |row: &Vec<i32>| row.iter().filter(only_negative).count() as i32;

        grid.iter().map(count_negative).sum()
    }
}
