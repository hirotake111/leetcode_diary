use std::collections::HashMap;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        // Populate frequencies hash map
        let mut frequencies = HashMap::new();
        nums.into_iter().for_each(|n| {
            *(frequencies.entry(n).or_insert(0)) += 1;
        });
        // Convert it in to a vector
        let mut frequency_vector: Vec<(i32, i32)> = frequencies.into_iter().collect();
        // Sort the vector by the 2nd element (counts)
        frequency_vector.sort_by(|a, b| b.1.cmp(&a.1));
        // Take the first k elements and return it as Vec<i32>
        frequency_vector
            .into_iter()
            .take(k as usize)
            .map(|(n, _)| n)
            .collect()
    }
}
