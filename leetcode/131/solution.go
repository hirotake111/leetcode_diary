package main

var backtrack func(i int) [][]string

func partition(s string) [][]string {
	dp := make([][][]string, len(s))

	backtrack = func(i int) [][]string {
		arr := [][]string{}
		if len(s) <= i {
			// No more strings to be processed -> return an empty array
			return [][]string{{}}
		}
		if dp[i] != nil {
			return dp[i]
		}
		if len(s[i:]) == 1 {
			// Only one character -> return it
			subArr := make([]string, 1)
			subArr[0] = string(s[i])
			arr = append(arr, subArr)
			dp[i] = arr
			return dp[i]
		}

		for j := i + 1; j <= len(s); j++ {
			subString := s[i:j]
			if validPalindrome(subString) {
				for _, palindromes := range backtrack(j) {
					palindromes = append([]string{subString}, palindromes...)
					arr = append(arr, palindromes)
				}
			}
		}
		dp[i] = arr
		return dp[i]
	}

	return backtrack(0)
}

func validPalindrome(s string) bool {
	i, j := 0, len(s)-1
	for i < j {
		if s[i] != s[j] {
			return false
		}
		i++
		j--
	}
	return true
}
