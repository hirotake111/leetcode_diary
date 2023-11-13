/**
 * https://leetcode.com/problems/sort-vowels-in-a-string/
 * 2785. Sort Vowels in a String
 */

impl Solution {
    pub fn sort_vowels(s: String) -> String {
        let mut copied: Vec<char> = s.chars().collect();
        let mut v_arr: Vec<char> = s.chars().filter(is_vowel).collect();

        if v_arr.len() == 0 {
            return s;
        }

        v_arr.sort_unstable();
        let mut i = 0;
        for (j, c) in s.chars().enumerate() {
            if is_vowel(&c) {
                copied[j] = v_arr[i];
                i += 1;
            }
        }

        copied.iter().collect::<String>()
    }
}

fn is_vowel(c: &char) -> bool {
    *c == 'A'
        || *c == 'E'
        || *c == 'I'
        || *c == 'O'
        || *c == 'U'
        || *c == 'a'
        || *c == 'e'
        || *c == 'i'
        || *c == 'o'
        || *c == 'u'
}
