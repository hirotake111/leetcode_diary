impl Solution {
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        match nums.len() {
            0 => vec![vec![]],
            1 => vec![nums],
            2 => vec![vec![nums[0], nums[1]], vec![nums[1], nums[0]]],
            l => {
                let mut result = vec![];
                for (i, &v) in nums.iter().enumerate() {
                    let mut nums = nums.clone();
                    nums.remove(i);
                    for mut sub_arr in Self::permute(nums) {
                        sub_arr.push(v);
                        result.push(sub_arr);
                    }
                }
                result
            }
        }
    }
}
