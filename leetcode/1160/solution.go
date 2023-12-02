/**
 * https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
 * 1160. Find Words That Can Be Formed by Characters
 */
package main

func countCharacters(words []string, chars string) int {
	base := toCounter(chars)
	total := 0
	for _, w := range words {
		flag := true
		for i, cnt := range toCounter(w) {
			if cnt > base[i] {
				flag = false
				break
			}
		}
		if flag {
			total += len(w)
		}
	}
	return total
}

func toCounter(s string) [26]int {
	arr := [26]int{}
	for _, b := range []byte(s) {
		i := b - 'a'
		arr[i] += 1
	}
	return arr
}
