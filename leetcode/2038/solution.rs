/**
 * https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
 * 2038. Remove Colored Pieces if Both Neighbors are the Same Color
 */
impl Solution {
    pub fn winner_of_game(colors: String) -> bool {
        let mut alice: usize = 0;
        let mut bob: usize = 0;

        for (a, b, c) in colors.as_bytes().windows(3).map(|x| (x[0], x[1], x[2])) {
            if a == b && b == c {
                if a == 65 {
                    alice += 1;
                } else {
                    bob += 1;
                }
            }
        }

        alice > bob
    }
}
