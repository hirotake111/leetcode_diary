impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        if nums.len() == 0 {
            return vec![];
        }

        let mut answer: Vec<String> = vec![];
        let (mut a, mut b) = (nums[0], nums[0]);
        let mut nums = nums.into_iter();
        nums.next();
        for n in nums {
            if n == b + 1 {
                // The current range continues
                b += 1;
                continue;
            }
            //  End of the current range -> add a string to the answer
            if a == b {
                answer.push(a.to_string());
            } else {
                answer.push(format!("{a}->{b}"));
            }
            // n should be the next a
            a = n;
            b = n;
        }

        if a == b {
            answer.push(a.to_string());
        } else {
            answer.push(format!("{a}->{b}"));
        }

        answer
    }
}
