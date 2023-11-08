/**
 * https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/
 * 2849. Determine if a Cell is Reachable at a Given Time
 */

impl Solution {
    pub fn is_reachable_at_time(sx: i32, sy: i32, fx: i32, fy: i32, t: i32) -> bool {
        let steps = (sx - fx).abs().max((sy - fy).abs());
        match t {
            0 => steps == 0,
            1 => steps > 0 && steps <= t,
            _ => steps <= t,
        }
    }
}
