/**
 * https://leetcode.com/problems/coin-change-ii/
 * 518. Coin Change II
 */
impl Solution {
    pub fn change(amount: i32, coins: Vec<i32>) -> i32 {
        let mut memo: Vec<i32> = vec![0; amount as usize + 1];
        memo[0] = 1;

        for coin in coins {
            if amount < coin {
                continue;
            }
            let coin = coin as usize;
            for rest in 1..=amount as usize {
                if coin <= rest {
                    memo[rest] += memo[rest - coin];
                }
            }
        }

        memo[amount as usize]
    }
}
