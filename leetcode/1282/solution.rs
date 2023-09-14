/**
 * https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/?envType=daily-question&envId=2023-09-11
 * 1282. Group the People Given the Group Size They Belong To
 */
impl Solution {
    pub fn group_the_people(group_sizes: Vec<i32>) -> Vec<Vec<i32>> {
        use std::collections::HashMap;
        let mut group_map: HashMap<i32, Vec<i32>> = HashMap::new();
        group_sizes.iter().enumerate().for_each(|(i, &size)| {
            group_map
                .entry(size)
                .and_modify(|v| v.push(i as i32))
                .or_insert(vec![i as i32]);
        });

        let mut groups: Vec<Vec<i32>> = vec![];
        group_map.iter().for_each(|(&size, people)| {
            people.chunks(size as usize).for_each(|chunk| {
                groups.push(chunk.to_vec());
            });
        });
        groups
    }
}
