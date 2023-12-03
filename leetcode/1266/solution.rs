/**
 * https://leetcode.com/problems/minimum-time-visiting-all-points/
 * 1266. Minimum Time Visiting All Points
 */
impl Solution {
    pub fn min_time_to_visit_all_points(points: Vec<Vec<i32>>) -> i32 {
        points
            .windows(2)
            .map(|p| (((p[0][0] - p[1][0]).abs()).max((p[0][1] - p[1][1]).abs())))
            .sum()
    }
}
