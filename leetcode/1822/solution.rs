impl Solution {
    pub fn array_sign(nums: Vec<i32>) -> i32 {
        nums.iter().fold(1, |a, &c| a * c.signum())
    }
}
