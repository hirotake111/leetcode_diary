/**
 * https://leetcode.com/problems/path-crossing/
 * 1496. Path Crossing
 */
package main

func isPathCrossing(path string) bool {
	x, y := 0, 0
	seen := make(map[Tuple]struct{})
	seen[Tuple{x, y}] = struct{}{}
	for _, c := range path {
		switch c {
		case 'N':
			y--
		case 'S':
			y++
		case 'W':
			x--
		default:
			x++
		}
		if _, ok := seen[Tuple{x, y}]; ok {
			return true
		}
		seen[Tuple{x, y}] = struct{}{}
	}
	return false
}

type Tuple struct {
	a, b int
}

func (t Tuple) Hash() uint64 {
	return uint64(t.a) ^ uint64(t.b)
}
func (t Tuple) Equal(other Tuple) bool {
	return t.a == other.a && t.b == other.b
}
