use std::collections::HashMap;

/**
 * DFS + Memoization approach
 */
impl Solution {
    pub fn predict_the_winner(nums: Vec<i32>) -> bool {
        let mut memo: HashMap<(usize, usize), i32> = HashMap::new();
        if nums.len() == 1 {
            // Player A always wins
            true
        } else {
            dfs(0, nums.len() - 1, &nums, &mut memo) >= 0
        }
    }
}

fn dfs(i: usize, j: usize, nums: &Vec<i32>, memo: &mut HashMap<(usize, usize), i32>) -> i32 {
    if i + 1 == j {
        // This player always pick up larger one (optimal move).
        (nums[i] - nums[j]).abs()
    } else if let Some(&n) = memo.get(&(i, j)) {
        // We can use memoized result
        n
    } else {
        // The player has two choices - pick up either a left most, or a right most element.
        let a = nums[i] - dfs(i + 1, j, nums, memo);
        let b = nums[j] - dfs(i, j - 1, nums, memo);
        // Choose larger one (optimal move)
        let result = a.max(b);
        // Store it to memo for later use.
        memo.insert((i, j), result);
        result
    }
}
