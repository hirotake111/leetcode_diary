#include <array>
#include <iostream>
#include <set>
#include <string>

using namespace std;

class Solution {
public:
  int minDeletions(string s) {
    int current = 0, deleteCount = 0;
    set<int> seen = {};
    array<int, 26> freq = {};

    for (char c : s) {
      freq[c - 'a']++;
    }

    for (int i = 0; i < 26; i++) {
      while (freq[i] && seen.find(freq[i]) != seen.end()) {
        freq[i]--;
        deleteCount++;
      }
      seen.insert(freq[i]);
    }

    return deleteCount;

    // int current = 0, deleteCount = 0;
    // set<int> seen;
    // array<int, 26> frequencies = {};

    // for (int i = 0; i < s.size(); i++)
    // frequencies[s[i] - 'a']++;

    // for (int n : frequencies) {
    // if (n == 0)
    // continue;

    // while (true) {
    // decltype(seen)::iterator pos = seen.find(n);
    // if (pos == seen.end() || n == 0)
    // break;

    // n--;
    // deleteCount++;
    // }

    // seen.insert(n);
    // }

    // return deleteCount;
  }
};

int main() {
  Solution s;
  string data = "aaabbbcccddd";
  int expected = 6;
  int result = s.minDeletions(data);
  if (result == expected) {
    cout << "done!" << endl;
  } else {
    cout << result << " != " << expected << endl;
  }
  return 0;
}