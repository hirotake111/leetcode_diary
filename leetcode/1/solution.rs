struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        use std::collections::HashMap;
        let mut hm: HashMap<i32, i32> = HashMap::new();
        for (idx_a, &n) in nums.iter().enumerate() {
            let idx_a = idx_a as i32;
            let diff = target - n;
            if let Some(&idx_b) = hm.get(&diff) {
                return vec![idx_a, idx_b];
            }
            hm.insert(n, idx_a);
        }
        vec![-1, -1]
    }
}
