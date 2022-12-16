// 232. Implement Queue using Stacks
// https://leetcode.com/problems/implement-queue-using-stacks/

package lc232

type MyQueue struct {
	s      []int
	top    int
	bottom int
}

func Constructor() MyQueue {
	return MyQueue{
		s:      []int{},
		top:    -1,
		bottom: -1,
	}

}

func (this *MyQueue) Push(x int) {
	this.s = append(this.s, x)
	if this.top == -1 {
		// no item in it -> init top indexes
		this.top, this.bottom = 0, 0
		return
	}
	// we have more than 0 items -> increment this.top
	this.top++
}

func (this *MyQueue) Pop() int {
	// pick up current item on the top
	v := this.Peek()
	if this.top == this.bottom {
		// we now have no items in it -> empty the slice
		this.s, this.bottom, this.top = nil, -1, -1
		return v
	}
	// we now have more than 0 element -> increment bottom
	this.bottom++
	return v
}

func (this *MyQueue) Peek() int {
	return this.s[this.bottom]
}

func (this *MyQueue) Empty() bool {
	return len(this.s) == 0
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */
