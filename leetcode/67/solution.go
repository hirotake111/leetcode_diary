/*
https://leetcode.com/problems/add-binary/
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.
*/
package main

import (
	"math/big"
)

func addBinary(a string, b string) string {
	x, y, z := new(big.Int), new(big.Int), new(big.Int)
	x.SetString(a, 2)
	y.SetString(b, 2)
	z.Add(x, y)
	return z.Text(2)
}

func main() {
	addBinary("11", "1")

}
