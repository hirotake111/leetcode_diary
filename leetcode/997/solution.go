/*
https://leetcode.com/problems/find-the-town-judge/v
997. Find the Town Judge

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
*/
package main

func findJudge(n int, trust [][]int) int {
	trusted := make(map[int]int)
	trusts := make(map[int]bool)

	// edge case
	if len(trust) == 0 {
		if n == 1 {
			return 1
		}
		return -1
	}
	for _, pair := range trust {
		a, b := pair[0], pair[1]
		trusted[b]++
		trusts[a] = true
	}

	maxIdx := trusted[n-1]
	for k, v := range trusted {
		if trusted[maxIdx] < v {
			maxIdx = k
		}
	}
	if trusted[maxIdx] != n-1 || trusts[maxIdx] {
		return -1
	}
	return maxIdx
}
