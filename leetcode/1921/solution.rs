/**
 * https://leetcode.com/problems/eliminate-maximum-number-of-monsters/
 * 1921. Eliminate Maximum Number of Monsters
 */
impl Solution {
    pub fn eliminate_maximum(dist: Vec<i32>, speed: Vec<i32>) -> i32 {
        let mut minutes = dist
            .iter()
            .zip(speed.iter())
            .map(|(d, s)| d / s + if d % s > 0 {1} else {0})
            .collect::<Vec<i32>>();

        minutes.sort_unstable();
        for (i, &n) in minutes.iter().enumerate() {
            let i = i as i32;
            if i >= n {
                return i;
            }
        }
        
        // killed all monsters
        dist.len() as i32
    }
