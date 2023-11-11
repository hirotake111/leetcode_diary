/**
 * https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/
 * 1743. Restore the Array From Adjacent Pairs
 */

impl Solution {
    pub fn restore_array(adjacent_pairs: Vec<Vec<i32>>) -> Vec<i32> {
        use std::collections::{HashMap, HashSet};
        let mut entries: HashSet<i32> = HashSet::new();
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();

        for p in adjacent_pairs {
            let (i, j) = (p[0], p[1]);
            graph.entry(i).and_modify(|v| v.push(j)).or_insert(vec![j]);
            graph.entry(j).and_modify(|v| v.push(i)).or_insert(vec![i]);
            if !entries.remove(&i) {
                entries.insert(i);
            }
            if !entries.remove(&j) {
                entries.insert(j);
            }
        }

        // at this point entries has exactly two elements in it.
        let entries: Vec<i32> = entries.into_iter().collect();
        let (mut cur, end) = (entries[0], entries[1]);
        let mut arr = vec![cur];
        let mut done: HashSet<i32> = vec![cur].into_iter().collect();
        while cur != end {
            let v = graph.get(&cur).unwrap();
            cur = if v.len() > 1 && !done.contains(&v[1]) {
                v[1]
            } else {
                v[0]
            };
            arr.push(cur);
            done.insert(cur);
        }

        arr
    }
}
