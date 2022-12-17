/*
150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/
*/
package lc150

import "strconv"

// Implement stack
type Stack []int

func (s *Stack) Push(item int) {
	*s = append(*s, item)
}

func (s *Stack) Pop() (item int) {
	index := len(*s) - 1
	item = (*s)[index]
	*s = (*s)[:index]
	return
}

func evalRPN(tokens []string) int {
	stack := Stack{}
	// A common way to create set in golang
	set := map[string]struct{}{"+": {}, "-": {}, "*": {}, "/": {}}

	for _, t := range tokens {
		_, ok := set[t]
		if !ok {
			// t is a number -> push it to the stack
			num, _ := strconv.Atoi(t)
			stack.Push(num)
			continue
		}
		// pick up two numbers from the stack
		b := stack.Pop()
		a := stack.Pop()
		if t == "+" {
			stack.Push(a + b)
		} else if t == "-" {
			stack.Push(a - b)
		} else if t == "*" {
			stack.Push(a * b)
		} else {
			sign := 1
			if a < 0 {
				a, sign = a*-1, -1
			}
			if b < 0 {
				b, sign = b*-1, sign*-1
			}
			stack.Push(a / b * sign)
		}
	}

	return stack[0]
}
