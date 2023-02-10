/*
https://leetcode.com/problems/as-far-from-land-as-possible/
1162. As Far from Land as Possible

Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.
The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
*/
package main

func maxDistance(grid [][]int) int {
	length, summary := len(grid), sum(&grid)

	// Edge case
	if summary == 0 || summary == length*length {
		return -1
	}

	visited := make([][]int, length)
	for i := range visited {
		visited[i] = make([]int, length)
	}
	directions := [4][2]int{{0, -1}, {1, 0}, {0, 1}, {-1, 0}}
	var queue [][2]int

	// Enqueue all islands
	for i := 0; i < length; i++ {
		for j := 0; j < length; j++ {
			if grid[i][j] == 1 {
				// Mark as visited and enque it
				visited[i][j] = 1
				queue = append(queue, [2]int{i, j})
			}
		}
	}

	distance := -1
	queueLength := len(queue)
	for 0 < queueLength {
		distance++
		for i := 0; i < queueLength; i++ {
			// Dequeue an item
			item := queue[0]
			queue = queue[1:]
			// Loop over directions
			for _, d := range directions {
				x, y := item[0]+d[0], item[1]+d[1]
				if (0 <= x && x < length) && (0 <= y && y < length) && visited[x][y] == 0 {
					// (x, y) is in the range of grid and we haven't visited yet.
					visited[x][y] = 1
					queue = append(queue, [2]int{x, y})
				}
			}
		}
		queueLength = len(queue)
	}

	return distance
}

func sum(arr *[][]int) int {
	result := 0
	for _, subArr := range *arr {
		for _, n := range subArr {
			result += n
		}
	}
	return result
}
