/**
 * https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
 * 1337. The K Weakest Rows in a Matrix
 */
impl Solution {
    pub fn k_weakest_rows(mat: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let mut arr: Vec<(i32, i32)> = mat
            .iter()
            .enumerate()
            .map(|(i, row)| (row.iter().sum(), i as i32))
            .collect();

        arr.sort();

        arr.iter().take(k).map(|&(_, i)| i).collect()
    }
}
