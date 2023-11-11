/**
 * https://leetcode.com/problems/design-graph-with-shortest-path-calculator/
 * 2642. Design Graph With Shortest Path Calculator
 */
use std::collections::{BinaryHeap, HashMap, HashSet};

struct Graph {
    graph: HashMap<usize, Vec<(i32, usize)>>,
}

impl Graph {
    fn new(n: i32, edges: Vec<Vec<i32>>) -> Self {
        let graph = HashMap::new();
        let mut graph: Graph = Graph { graph };
        edges.into_iter().for_each(|edge| graph.add_edge(edge));
        graph
    }

    fn add_edge(&mut self, edge: Vec<i32>) {
        // since Rust's binary heap is max-heap we will store cost * -1
        let (from, to, cost) = (edge[0] as usize, edge[1] as usize, -edge[2]);
        self.graph
            .entry(from)
            .and_modify(|v| v.push((cost, to)))
            .or_insert(vec![(cost, to)]);
    }

    fn shortest_path(&self, node1: i32, node2: i32) -> i32 {
        let node1 = node1 as usize;
        let node2 = node2 as usize;
        let mut costs: HashMap<usize, i32> = HashMap::new();
        let mut seen: HashSet<usize> = HashSet::new();
        let mut heap: BinaryHeap<(i32, usize)> = BinaryHeap::new();
        heap.push((0, node1));

        while let Some((cost, node)) = heap.pop() {
            if node == node2 {
                // found the shortest path
                return -cost;
            }

            // update costs
            costs
                .entry(node)
                .and_modify(|v| *v = cost.min(*v))
                .or_insert(cost);

            // push neighbors
            if seen.contains(&node) {
                continue;
            }
            seen.insert(node);
            if let Some(neighbors) = self.graph.get(&node) {
                for (n_cost, neighbor) in neighbors {
                    let cost = cost + *n_cost;
                    heap.push((cost, *neighbor));
                }
            }
        }

        -1
    }
}
