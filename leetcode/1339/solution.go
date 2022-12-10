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

func getTotal(node *TreeNode) int {
	if node == nil {
		return 0
	}
	return getTotal(node.Left) + getTotal(node.Right) + node.Val
}

var total int
var product int

func getProduct(node *TreeNode) int {
	if node == nil {
		return 0
	}
	currentSum := getProduct(node.Left) + getProduct(node.Right) + node.Val
	cur_product := (total - currentSum) * currentSum
	product = max(product, cur_product)
	return currentSum
}

func maxProduct(root *TreeNode) int {

	total = getTotal(root)
	product = 0
	getProduct(root)
	return product % 1000000007
}
