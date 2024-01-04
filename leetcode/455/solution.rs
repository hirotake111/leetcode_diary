/**
 * https://leetcode.com/problems/assign-cookies/
 * 455. Assign Cookies
 */
impl Solution {
    pub fn find_content_children(mut g: Vec<i32>, mut s: Vec<i32>) -> i32 {
        g.sort_unstable();
        s.sort_unstable();
        let (mut i, mut j) = (0, 0);
        while i < g.len() && j < s.len() {
            if s[j] >= g[i] {
                i += 1
            }
            j += 1;
        }
        i as i32
    }
}
