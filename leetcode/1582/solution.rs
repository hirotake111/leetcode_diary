/**
 * https://leetcode.com/problems/special-positions-in-a-binary-matrix/
 * 1582. Special Positions in a Binary Matrix
 */
impl Solution {
    pub fn num_special(mat: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (mat.len(), mat[0].len());
        let mut rows = vec![0; m];
        let mut cols = vec![0; n];

        for i in 0..m {
            for j in 0..n {
                rows[i] += mat[i][j];
                cols[j] += mat[i][j];
            }
        }

        let mut total = 0;
        for (i, _) in rows.iter().enumerate().filter(|(i, x)| **x == 1) {
            for (j, _) in cols.iter().enumerate().filter(|(i, x)| **x == 1) {
                if mat[i][j] == 1 {
                    total += 1;
                }
            }
        }

        total
    }
}
