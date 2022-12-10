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
	Node    *TreeNode
	Total   int
	Product int
}

func (s *Solution) getTotal(node *TreeNode) int {
	if node == nil {
		return 0
	}
	return s.getTotal(node.Left) + s.getTotal(node.Right) + node.Val
}

func (s *Solution) UpdateTotal() {
	s.Total = s.getTotal(s.Node)
}

func (s *Solution) GetProduct(node *TreeNode) int {
	if node == nil {
		return 0
	}
	currentSum := s.GetProduct(node.Left) + s.GetProduct(node.Right) + node.Val
	product := currentSum * (s.Total - currentSum)
	s.Product = max(s.Product, product)
	return currentSum
}
func (s *Solution) UpdateProdct() {
	s.UpdateTotal()
	s.GetProduct(s.Node)
}

func NewSolution(root *TreeNode) Solution {
	s := Solution{Total: 0, Product: 0, Node: root}
	s.UpdateProdct()
	return s
}

func maxProduct(root *TreeNode) int {
	s := NewSolution(root)
	return s.Product % 1000000007
}
