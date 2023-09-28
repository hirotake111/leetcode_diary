impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut i = 0;
        let mut prev = -101;
        for j in 0..nums.len() {
            if prev < nums[j] {
                prev = nums[j];
                nums[i] = prev;
                i += 1;
            }
        }
        i as i32
    }
}
