/**
 * https://leetcode.com/problems/01-matrix/
 * 542. 01 Matrix
 */
use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn update_matrix(mat: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut queue: VecDeque<(i32, i32)> = VecDeque::new();
        let (m, n) = (mat.len(), mat[0].len());
        let directions = [(0, -1), (1, 0), (0, 1), (-1, 0)];
        let mut answer = vec![vec![i32::MAX; n]; m];

        // Pick up all zeroes
        for row in 0..m {
            for col in 0..n {
                if mat[row][col] == 0 {
                    answer[row][col] = 0;
                    let (row, col) = (row as i32, col as i32);
                    queue.push_back((row, col));
                }
            }
        }

        while let Some((p_row, p_col)) = queue.pop_front() {
            for (row, col) in directions.iter().map(|d| (p_row + d.0, p_col + d.1)) {
                if row < 0 || m <= row as usize || col < 0 || n <= col as usize {
                    // Out of bound
                    continue;
                }
                if answer[row as usize][col as usize] != i32::MAX {
                    // Already visited
                    continue;
                }
                answer[row as usize][col as usize] = answer[p_row as usize][p_col as usize] + 1;
                queue.push_back((row, col));
            }
        }
        answer
    }
}
