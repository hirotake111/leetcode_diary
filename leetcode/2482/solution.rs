/**
 * https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/
 * 2482. Difference Between Ones and Zeros in Row and Column
 */
impl Solution {
    pub fn ones_minus_zeros(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let (m, n) = (grid.len(), grid[0].len());
        let mut rows: Vec<i32> = vec![0; m];
        let mut cols: Vec<i32> = vec![0; n];
        for i in 0..m {
            for j in 0..n {
                rows[i] += grid[i][j];
                cols[j] += grid[i][j];
            }
        }

        let mn = (m + n) as i32;
        (0..m)
            .map(|i| (0..n).map(|j| (rows[i] + cols[j]) * 2 - mn).collect())
            .collect()
        //let mut diff = vec![vec![0;n];m];
        //for i in 0..m {
        //    for j in 0..n {
        //        diff[i][j] = (rows[i] + cols[j]) * 2 - mn;
        //    }
        //}
        //diff
    }
}
