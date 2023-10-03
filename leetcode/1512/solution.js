/**
 * https://leetcode.com/problems/number-of-good-pairs/
 * 1512. Number of Good Pairs
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function (nums) {
  const arr = new Array(101).fill(0);
  let count = 0;

  for (const n of nums) {
    count += arr[n];
    arr[n] += 1;
  }
  return count;
};
