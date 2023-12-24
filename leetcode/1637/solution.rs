/**
 * https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
 * 1637. Widest Vertical Area Between Two Points Containing No Points
 */
impl Solution {
    pub fn max_width_of_vertical_area(points: Vec<Vec<i32>>) -> i32 {
        let mut points: Vec<i32> = points.into_iter().map(|v| v[0]).collect();
        points.sort_unstable();
        points
            .windows(2)
            .fold(0, |acc, cur| acc.max(cur[1] - cur[0]))
    }
}
