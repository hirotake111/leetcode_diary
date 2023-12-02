/**
 * https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
 * 1160. Find Words That Can Be Formed by Characters
 */
impl Solution {
    pub fn count_characters(words: Vec<String>, chars: String) -> i32 {
        let base = to_arr(&chars);
        let mut total = 0;
        for word in words {
            let mut can_form = true;
            for (&count, base_count) in to_arr(&word).iter().zip(base) {
                if count > base_count {
                    can_form = false;
                    break;
                }
            }
            if can_form {
                total += word.len();
            }
        }

        total as i32
    }
}

fn to_arr(s: &str) -> [i32; 26] {
    let mut arr = [0; 26];
    for b in s.bytes() {
        let i = (b - b'a') as usize;
        arr[i] += 1;
    }
    arr
}
