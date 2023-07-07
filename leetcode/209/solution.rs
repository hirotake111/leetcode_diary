impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        // Sliding window approach
        let mut slow: usize = 0;
        let mut total: i32 = 0;
        let mut answer = usize::MAX;
        for (fast, v) in nums.iter().enumerate() {
            total += v;
            while target <= total {
                // We found a possible candidate -> update answer
                answer = answer.min(fast - slow + 1);
                // Shrink total and slow index
                total -= nums[slow];
                slow += 1;
            }
        } 

        if answer == usize::MAX {
            // No sub arrays found
            0 
        } else {
            answer as i32
        }
    }
