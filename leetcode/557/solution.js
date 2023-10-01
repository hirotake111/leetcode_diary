/**
 * https://leetcode.com/problems/reverse-words-in-a-string-iii/
 * 557. Reverse Words in a String III
 */

/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  return s
    .split(" ")
    .map((w) => w.split("").reverse().join(""))
    .join(" ");
};
