/**
 * https://leetcode.com/problems/path-crossing/
 * 1496. Path Crossing
 */
use std::collections::HashSet;

impl Solution {
    pub fn is_path_crossing(path: String) -> bool {
        let (mut x, mut y) = (0, 0);
        let mut seen = HashSet::new();
        seen.insert((x, y));
        for c in path.chars() {
            match c {
                'N' => y -= 1,
                'S' => y += 1,
                'E' => x += 1,
                _ => x -= 1,
            }
            if seen.contains(&(x, y)) {
                return true;
            }
            seen.insert((x, y));
        }

        false
    }
}
