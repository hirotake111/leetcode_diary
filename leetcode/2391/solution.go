/**
 * https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/
 * 2391. Minimum Amount of Time to Collect Garbage
 */
package main

func garbageCollection(garbage []string, travel []int) int {
	var total, M, P, G int

	for i := 1; i < len(travel); i++ {
		travel[i] += travel[i-1]
	}

	for i, s := range garbage {
		for _, x := range s {
			switch x {
			case 'M':
				M = i
			case 'P':
				P = i
			default:
				G = i
			}
			total++
		}
	}

	if M > 0 {
		total += travel[M-1]
	}
	if P > 0 {
		total += travel[P-1]
	}
	if G > 0 {
		total += travel[G-1]
	}

	return total
}
