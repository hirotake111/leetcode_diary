/**
 * https://leetcode.com/problems/maximal-network-rank/
 * 1615. Maximal Network Rank
 *
 * According to the constrains, there are at most 100 cities in the network.
 * Therefore, it should be acceptable to use a brute force approach.
 * 1. Create a graph
 * 2. For each pair of cities, calculate the rank of the pair (which is the sum of all connected cities)
 * 3. If the two cities are connected, then the rank is reduced by 1.
 */

impl Solution {
    pub fn maximal_network_rank(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        // Create a graph
        let n = n as usize;
        let mut graph: Vec<Vec<usize>> = (0..n).map(|_| vec![]).collect();
        for (a, b) in roads.iter().map(|r| (r[0], r[1])) {
            let (a, b) = (a as usize, b as usize);
            graph[a].push(b);
            graph[b].push(a);
        }

        let mut highest_rank = 0;
        for i in 0..n {
            for j in (i + 1)..n {
                let rank = graph[i].len() + graph[j].len();
                let connected = match graph[i].iter().find(|&&x| x == j) {
                    Some(_) => 1,
                    None => 0,
                };
                highest_rank = highest_rank.max(rank - connected);
            }
        }
        highest_rank as i32
    }
}
