impl Solution {
    pub fn longest_subsequence(arr: Vec<i32>, difference: i32) -> i32 {
        use std::collections::HashMap;
        let mut hm = HashMap::new();
        let mut longest = 0;

        for value in arr {
            let prev_value = value - difference;
            let counts = if let Some(v) = hm.get(&prev_value) {
                v + 1
            } else {
                1
            };
            hm.insert(value, counts);
            longest = longest.max(counts);
        }

        longest
    }
}
