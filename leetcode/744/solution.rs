impl Solution {
    pub fn next_greatest_letter(letters: Vec<char>, target: char) -> char {
        let i = letters.partition_point(|c| c <= &target);
        if i == letters.len() {
            letters[0]
        } else {
            letters[i]
        }
        // *letters
        //     .iter()
        //     .filter(|&&c| target < c)
        //     .next()
        //     .unwrap_or(&letters[0])
    }
}
