package main

/*
https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
1061. Lexicographically Smallest Equivalent String

You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.
*/

func smallestEquivalentString(s1 string, s2 string, baseStr string) string {
	uf := NewUnioinFind(s1, s2)
	return uf.getString(baseStr)
}

type UnionFind struct {
	tree []int
}

func NewUnioinFind(s1, s2 string) *UnionFind {
	// Crate a tree
	tree := make([]int, 26)
	for i := range tree {
		tree[i] = i
	}

	uf := UnionFind{tree: tree}
	uf.union(s1, s2)
	return &uf
}

func (uf *UnionFind) find(idx int) int {
	root := uf.tree[idx]
	if root == idx {
		return idx
	}
	// Find root recursively
	root = uf.find(uf.tree[idx])
	uf.tree[idx] = root
	return root
}

func (uf *UnionFind) union(s1, s2 string) {
	for i, c := range s1 {
		if int(c) == int(s2[i]) {
			// Do nothing and go to next
			continue
		}
		// Find root for s1 and s2 in the first place
		root_1 := uf.find(int(c) - 97)
		root_2 := uf.find(int(s2[i]) - 97)
		// Set root
		if root_1 < root_2 {
			uf.tree[root_2] = root_1
		} else {
			uf.tree[root_1] = root_2
		}
	}
}

func (uf *UnionFind) getString(baseStr string) string {
	runes := []rune(baseStr)
	for i, c := range baseStr {
		root := uf.find(int(c) - 97)
		runes[i] = rune(root + 97)
	}
	return string(runes)
}
