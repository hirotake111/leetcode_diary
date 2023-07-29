/**
 * https://leetcode.com/problems/soup-servings/description/
 * 808. Soup Servings
 */
// DFS + DP approach
use std::collections::HashMap;

impl Solution {
    pub fn soup_servings(n: i32) -> f64 {
        if n > 4800 {
            1.
        } else {
            dfs(n, n, &mut HashMap::new())
        }
    }
}

fn dfs(a: i32, b: i32, dp: &mut HashMap<(i32, i32), f64>) -> f64 {
    if let Some(&v) = dp.get(&(a, b)) {
        return v;
    }

    match (a <= 0, b <= 0) {
        (true, true) => 0.5,
        (false, true) => 0.,
        (true, false) => 1.,
        _ => {
            let result = (dfs(a - 100, b, dp)
                + dfs(a - 75, b - 25, dp)
                + dfs(a - 50, b - 50, dp)
                + dfs(a - 25, b - 75, dp))
                / 4.0;
            dp.insert((a, b), result);
            result
        }
    }
}
