/*
https://leetcode.com/problems/zigzag-conversion/
6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
*/

package main

func convert(s string, numRows int) string {
	zigzag, col := -1, 0
	rows := make([]string, numRows)

	if numRows == 1 {
		return s
	}

	for _, c := range s {
		// Append character to row
		rows[col] += string(c)
		// Update zigzag
		if col == 0 || col == numRows-1 {
			zigzag *= -1
		}
		// Increment (or decrement) col
		col += zigzag
	}

	// Concatenate strings
	var answer string
	for _, str := range rows {
		answer += str
	}
	return answer
}
