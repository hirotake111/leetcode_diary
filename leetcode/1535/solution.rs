/**
 * https://leetcode.com/problems/find-the-winner-of-an-array-game/
 * 1535. Find the Winner of an Array Game
 */

impl Solution {
    pub fn get_winner(arr: Vec<i32>, k: i32) -> i32 {
        // Shortcut
        if arr.len() < k as usize {
            return arr.into_iter().max().unwrap();
        }

        let (mut count, mut winner, mut i) = (0, 0, 0);
        while count < k {
            if arr[winner] > arr[i] {
                count += 1;
            } else if arr[winner] < arr[i] {
                count = 1;
                winner = i;
            }
            i = (i + 1) % arr.len();
        }

        arr[winner]
    }
}
