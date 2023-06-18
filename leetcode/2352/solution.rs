/* Trie data structure approach */
use std::{collections::HashMap, hash::Hash, ops::Add};

impl Solution {
    pub fn equal_pairs(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        // Create a Trie
        let mut trie: Trie<i32, i32> = Trie::new();
        for col in 0..n {
            let key: Vec<i32> = (0..n).map(|row| grid[row][col]).collect();
            trie.insert(key, 1);
        }
        // Search
        let answer = grid
            .into_iter()
            .fold(0, |a, k| a + trie.get(k).unwrap_or(&0));
        answer
    }
}

#[derive(Debug, Default)]
struct Node<Key: Default, Value: Default + Add<Output = Value>> {
    value: Option<Value>,
    children: HashMap<Key, Node<Key, Value>>,
}

#[derive(Debug, Default)]
struct Trie<Key, Value>
where
    Key: Default + Eq + Hash,
    Value: Default + Add<Output = Value>,
{
    root: Node<Key, Value>,
}

impl<Key, Value> Trie<Key, Value>
where
    Key: Default + Eq + Hash,
    Value: Default + Add<Output = Value>,
{
    fn new() -> Self {
        Self {
            root: Node::default(),
        }
    }

    pub fn insert(&mut self, key: impl IntoIterator<Item = Key>, value: Value)
    where
        Key: Eq + Hash,
        Value: Default + Add<Output = Value> + std::ops::AddAssign,
    {
        let mut node = &mut self.root;
        for c in key.into_iter() {
            node = node.children.entry(c).or_insert_with(Node::default);
        }
        if let Some(v) = node.value.as_mut() {
            *v += value;
        } else {
            node.value = Some(value);
        }
    }

    pub fn get(&mut self, key: impl IntoIterator<Item = Key>) -> Option<&Value> {
        let mut node = &mut self.root;
        for k in key.into_iter() {
            if let Some(n) = node.children.get_mut(&k) {
                node = n;
            } else {
                return None;
            }
        }
        node.value.as_ref()
    }
}

// use std::collections::HashMap;

// struct Solution {}
// impl Solution {
// pub fn equal_pairs(grid: Vec<Vec<i32>>) -> i32 {
// let n = grid.len();
// let mut answer = 0;

// // Create a hash map
// let mut hash_map: HashMap<Vec<i32>, i32> = HashMap::with_capacity(n);
// for col in 0..n {
// let line: Vec<i32> = (0..n).map(|row| grid[row][col]).collect();
// if let Some(v) = hash_map.get_mut(&line) {
// *v += 1;
// } else {
// hash_map.insert(line, 1);
// }
// }

// // Search each key
// let answer = grid
// .iter()
// .fold(0, |a, line| a + hash_map.get(line).unwrap_or(&0));

// answer
// }
// }
