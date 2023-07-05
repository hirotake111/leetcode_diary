impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let mut slow = 0;
        let mut skip = 1;
        let mut answer = 0;
        for fast in 0..nums.len() {
            if nums[fast] == 0 {
                skip -= 1;
            }
            // Move slow pointer until we find next one
            while skip < 0 {
                if nums[slow] == 0 {
                    skip += 1;
                }
                slow += 1;
            }
            answer = answer.max(fast - slow);
        }

        answer as i32
    }
}
