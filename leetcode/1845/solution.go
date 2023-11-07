/**
 * https://leetcode.com/problems/seat-reservation-manager/
 * 1845. Seat Reservation Manager
 */
package main

import "container/heap"

type SeatManager struct {
	queue *IntHeap
}

func Constructor(n int) SeatManager {
	h := &IntHeap{}
	for i := 1; i <= n; i++ {
		heap.Push(h, i)
	}
	return SeatManager{queue: h}
}

func (this *SeatManager) Reserve() int {
	return heap.Pop(this.queue).(int)
}

func (this *SeatManager) Unreserve(seatNumber int) {
	heap.Push(this.queue, seatNumber)
}

type IntHeap []int

func (h IntHeap) Len() int {
	return len(h)
}

func (h IntHeap) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h IntHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *IntHeap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
