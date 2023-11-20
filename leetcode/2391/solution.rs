/**
 * https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/
 * 2391. Minimum Amount of Time to Collect Garbage
 */

impl Solution {
    pub fn garbage_collection(garbage: Vec<String>, mut travel: Vec<i32>) -> i32 {
        let mut total = 0;
        let (mut mi, mut pi, mut gi) = (0, 0, 0); // last index of each garbage

        for i in 1..travel.len() {
            travel[i] += travel[i - 1];
        }

        for (i, g) in garbage.iter().enumerate() {
            for c in g.chars() {
                match c {
                    'M' => mi = i,
                    'P' => pi = i,
                    _ => gi = i,
                }
                total += 1;
            }
        }

        if mi != 0 {
            total += travel[mi - 1];
        }
        if pi != 0 {
            total += travel[pi - 1];
        }
        if gi != 0 {
            total += travel[gi - 1];
        }

        total
    }
}
