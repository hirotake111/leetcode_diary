/**
 * https://leetcode.com/problems/unique-paths/description/
 * 62. Unique Paths
 */
impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        let (m, n) = (m as usize, n as usize);
        let mut memo: Vec<i32> = vec![0; n];
        memo[0] = 1;

        for _ in 0..m {
            for i in 1..n {
                memo[i] += memo[i - 1];
            }
        }

        memo[n - 1]
    }
}
