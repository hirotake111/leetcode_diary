#include "iostream"
#include "vector"

using namespace std;

class Solution {
public:
  vector<int> searchRange(vector<int> &nums, int target) {
    int l = nums.size();
    int i = l / 2;
    int min = 0, max = l - 1;
    int begin = -1, end = -1;

    if (l == 0 || nums.front() > target || nums.back() < target) {
      return {-1, -1};
    }

    while (true) {
      if (min == max) {
        break;
      }
      if (nums[i] == target) {
        int begin = target, end = target;
        while (0 <= begin - 1 && nums[begin - 1] == target) {
          begin--;
        }
        while (end + 1 < l && nums[end + 1] == target) {
          end++;
        }
        break;
      }

      if (nums[i] < target) {
        i += (l - min) / 2;
        min = i;
      } else {
        i -= (l - i) / 2;
        max = i;
      }
    }

    return {begin, end};
  }
};

int main() {
  // Solution s = Solution();
  // vector<int> v = {5, 7, 7, 8, 8, 10};
  int expected[2] = {3, 4};

  for (auto item : expected) {
    std::cout << item << " ";
  }
  if (expected == expected) {
    std::cout << "correct" << std::endl;
  } else {
    std::cout << "wrong" << std::endl;
  }
  return 0;
}