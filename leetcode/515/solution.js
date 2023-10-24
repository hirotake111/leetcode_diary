/**
 * https://leetcode.com/problems/find-largest-value-in-each-tree-row/
 * 515. Find Largest Value in Each Tree Row
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var largestValues = function (root) {
  const answer = [];
  const queue = [root];
  const MAX = (Math.pow(2, 31) + 1) * -1;
  if (!root) return [];

  while (queue.length) {
    const l = queue.length;
    let maxValue = MAX;
    for (let i = 0; i < l; i++) {
      const node = queue.shift();
      maxValue = Math.max(maxValue, node.val);
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    answer.push(maxValue);
  }
  return answer;
};
