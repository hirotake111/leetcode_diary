// 841. Keys and Rooms
// https://leetcode.com/problems/keys-and-rooms/
package lc841

var locked map[int]int
var dfs func(room int)

func canVisitAllRooms(rooms [][]int) bool {
	locked = make(map[int]int)
	for i := 1; i < len(rooms); i++ {
		locked[i] = i
	}

	dfs = func(room int) {
		// Pick up a key in the room
		for _, key := range rooms[room] {
			// Check to see if the corresponding room is unlocked
			if _, ok := locked[key]; ok {
				// Unlock it
				delete(locked, key)
				// And then go to the next
				dfs(key)
			}
		}
	}

	// Use the key to 0
	dfs(0)
	return len(locked) == 0
}
