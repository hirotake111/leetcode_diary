#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int maxScore(vector<int> &cardPoints, int k) {
    int current = 0;
    int length = cardPoints.size();

    for (int i = 0; i < k; i++) {
      current += cardPoints[i];
    }

    int answer = current;

    for (int j = 0; j < k; j++) {
      int prev = cardPoints[k - j - 1];
      int next = cardPoints[length - j - 1];
      current = current + next - prev;
      answer = max(answer, current);
    }

    return answer;
  }
};

struct Data {
  vector<int> cardPoints;
  int k;
  int expected;
};

int main() {
  Solution s;
  vector<Data> data = {{{1, 2, 3, 4, 5, 6, 1}, 3, 12}};

  for (int i = 0; i < data.size(); i++) {
    Data x = data[i];
    int result = s.maxScore(x.cardPoints, x.k);
    if (result != x.expected) {
      cout << "test failed: " << result << " != " << x.expected << endl;
    }
    cout << "done!" << endl;
  }
  return 0;
}