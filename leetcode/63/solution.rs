/**
 * https://leetcode.com/problems/unique-paths-ii/
 * 63. Unique Paths II
 */
impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (obstacle_grid.len(), obstacle_grid[0].len());
        let mut memo: Vec<i32> = vec![0; n];
        memo[0] = 1;

        // Edge case
        if obstacle_grid[0][0] == 1 || obstacle_grid[m - 1][n - 1] == 1 {
            return 0;
        }

        for row in obstacle_grid {
            for i in 0..n {
                if row[i] == 1 {
                    memo[i] = 0;
                } else if i > 0 {
                    memo[i] += memo[i - 1];
                }
            }
        }

        memo[n - 1]
    }
}
