impl Solution {
    pub fn can_make_arithmetic_progression(mut arr: Vec<i32>) -> bool {
        arr.sort();
        for w in arr.windows(3) {
            if w[2] - w[1] != w[1] - w[0] {
                return false;
            }
        }
        true
    }
}
