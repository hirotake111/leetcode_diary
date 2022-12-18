/*
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/
*/
package lc739

// Stack of indexes
type Stack []int

func (s *Stack) isEmpty() bool {
	return len(*s) == 0
}

/*
peak returns:

  - value of the peak item

  - index of the peak item

  - true if succeeded
*/
func (s *Stack) peak() (int, int, bool) {
	if s.isEmpty() {
		return -1, -1, false
	}
	last := len(*s) - 1
	return (*s)[last], last, true
}
func (s *Stack) push(item int) {
	*s = append(*s, item)
}
func (s *Stack) pop() (int, bool) {
	item, idx, ok := s.peak()
	if !ok {
		return 0, false
	}
	*s = (*s)[0:idx]
	return item, true
}

func dailyTemperatures(temperatures []int) []int {
	// Initialize stack
	stack := Stack{}
	// Initialize answer array with value of 0
	answer := make([]int, len(temperatures))
	for i := 0; i < len(temperatures); i++ {
		answer[i] = 0
	}

	// Loop over temperatures
	for idx, tmpl := range temperatures {
		// Loop while the stack has an item and
		// the current temperature is greater than the peak in the stack
		peakIdx, _, hasItem := stack.peak()
		for hasItem && temperatures[peakIdx] < tmpl {
			targetIdx, _ := stack.pop()
			answer[targetIdx] = idx - targetIdx
			peakIdx, _, hasItem = stack.peak()
		}
		// Now the stack is empty or the peak item in the stack is leass than
		// or equal to the current one.
		// -> just push it onto the stack
		stack.push(idx)
	}
	return answer
}
