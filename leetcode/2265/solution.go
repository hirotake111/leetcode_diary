// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
// 2265. Count Nodes Equal to Average of Subtree

func averageOfSubtree(root *TreeNode) int {
	count := 0

	dfs(root, &count)
	return count
}

func dfs(node *TreeNode, rc *int) (int, int) {
	if node == nil {
		return 0, 0
	}
	tl, nl := dfs(node.Left, rc)
	tr, nr := dfs(node.Right, rc)
	total := tl + tr + node.Val
	nums := nl + nr + 1
	if total/nums == node.Val {
		*rc += 1
	}

	return total, nums
}
