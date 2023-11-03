/**
 * https://leetcode.com/problems/build-an-array-with-stack-operations/
 * 1441. Build an Array With Stack Operations
 */

package main

func buildArray(target []int, n int) []string {
	i := 0
	ops := make([]string, 0, len(target))

	for c := 1; c <= n; c++ {
		ops = append(ops, "Push")
		if c != target[i] {
			ops = append(ops, "Pop")
		} else {
			i++
			if i == len(target) {
				break
			}
		}
	}

	return ops
}
