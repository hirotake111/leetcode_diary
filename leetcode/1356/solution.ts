// https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
// 1356. Sort Integers by The Number of 1 Bits

function sortByBits(arr: number[]): number[] {
  return arr.sort(byOnes);
}

function byOnes(a: number, b: number): number {
  const countA = countOnes(a);
  const countB = countOnes(b);
  return countA === countB ? a - b : countA - countB;
}

function countOnes(x: number): number {
  return x !== 0 ? (x & 1) + countOnes(x >> 1) : 0;
}
