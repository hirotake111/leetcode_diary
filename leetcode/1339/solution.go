package lc1339

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

type Solution struct {
	total   int
	Product int
}

func (s *Solution) getTotal(node *TreeNode) {
	var dfs func(*TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		return dfs(node.Left) + dfs(node.Right) + node.Val
	}
	s.total = dfs(node)
}

func (s *Solution) getProduct(node *TreeNode) int {
	if node == nil {
		return 0
	}
	currentSum := s.getProduct(node.Left) + s.getProduct(node.Right) + node.Val
	product := currentSum * (s.total - currentSum)
	s.Product = max(s.Product, product)
	return currentSum
}

func maxProduct(root *TreeNode) int {
	s := Solution{total: 0, Product: 0}
	s.getTotal(root)
	s.getProduct(root)

	return s.Product % 1000000007
}
