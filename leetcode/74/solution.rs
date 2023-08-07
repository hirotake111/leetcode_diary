/**
 * https://leetcode.com/problems/search-a-2d-matrix/
 * 74. Search a 2D Matrix
 *
 * Approach:
 * - According to the problem description we can see the 2D matrix as 1D array.
 * - Therefore you can convert it a basic binary search problem.
 * - The tricky part is, you need to convert a set of indexes of row and colum into an index, and then make it back to the original.
 */
impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let (m, n) = (matrix.len(), matrix[0].len());
        if target < matrix[0][0] || matrix[m - 1][n - 1] < target {
            return false;
        }
        if matrix[0][0] == target || matrix[m - 1][n - 1] == target {
            return true;
        }

        let mut begin = 0;
        let mut end = m * n - 1;
        while begin < end {
            let mid = (begin + end) / 2;
            let (row, col) = (mid / n, mid % n);
            if matrix[row][col] == target {
                return true;
            }
            if matrix[row][col] < target {
                begin = mid + 1;
            } else {
                end = mid;
            }
        }

        // Now begin points to the index of the target (or the closest value)
        matrix[begin / n][begin % n] == target
    }
}
