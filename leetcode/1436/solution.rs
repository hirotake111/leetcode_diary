/**
 * https://leetcode.com/problems/destination-city/
 * 1436. Destination City
 */
func destCity(paths [][]string) string {
    starts := make(map[string]struct{})
    for _, p := range paths {
        starts[p[0]] = struct{}{}
    }
    for _, p := range paths {
        if _, ok := starts[p[1]]; !ok {
            return p[1]
        }
    }
    panic("unreachable")
}