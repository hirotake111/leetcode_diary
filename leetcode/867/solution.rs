/**
 * https://leetcode.com/problems/transpose-matrix/
 * 867. Transpose Matrix
 */

impl Solution {
    pub fn transpose(matrix: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let (m, n) = (matrix.len(), matrix[0].len());
        let mut new_matrix: Vec<Vec<i32>> = (0..n).map(|_| Vec::with_capacity(m)).collect();

        for i in (0..m) {
            for j in (0..n) {
                new_matrix[j].push(matrix[i][j]);
            }
        }
        new_matrix
    }
}
