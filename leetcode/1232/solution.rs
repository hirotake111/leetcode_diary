// https://leetcode.com/problems/check-if-it-is-a-straight-line/
// 1232. Check If It Is a Straight Line
// You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

impl Solution {
    pub fn check_straight_line(coordinates: Vec<Vec<i32>>) -> bool {
        for w in coordinates.windows(3) {
            let (x, y, z) = (&w[0], &w[1], &w[2]);
            if (y[1] - x[1]) * (z[0] - y[0]) != (z[1] - y[1]) * (y[0] - x[0]) {
                return false;
            }
        }
        true
    }
}
