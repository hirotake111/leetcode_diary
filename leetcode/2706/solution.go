/**
 * https://leetcode.com/problems/buy-two-chocolates/
 * 2706. Buy Two Chocolates
 */
package main

func buyChoco(prices []int, money int) int {
	a, b := 101, 101
	for _, p := range prices {
		if p < a {
			b, a = a, p
		} else if p < b {
			b = p
		}
	}
	if a+b <= money {
		return money - a - b
	}
	return money
	// sort.Ints(prices)
	//if prices[0] + prices[1] <= money {
	//    return money - prices[0] - prices[1]
	//}
	//return money
}
