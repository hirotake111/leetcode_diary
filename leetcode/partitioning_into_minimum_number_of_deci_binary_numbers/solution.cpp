#include <string>
using namespace std;

class Solution {
public:
  int minPartitions(string n) {
    return *max_element(n.begin(), n.end()) - '0';
    // int ans = 0;
    // for (int i = 0; i < n.size(); i++)
    // ans = max(ans, n[i] - '0');

    // return ans;
  }
};