impl Solution {
    pub fn get_averages(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let n = (k * 2 + 1);
        let l = nums.len();
        let mut avgs = vec![-1; l];

        // Edge cage
        if l < k * 2 + 1 {
            return avgs;
        }

        // sum of values from nums[0 to (k * 2 - 1)]
        // e.g. if k =3, then total = nums[0 to 5]
        let mut total: i64 = (0..k * 2).map(|i| nums[i] as i64).sum();

        for i in (k..(l - k)) {
            total += nums[i + k] as i64;
            avgs[i] = (total / (n as i64)) as i32;
            total -= nums[i - k] as i64;
        }

        avgs
    }
}
