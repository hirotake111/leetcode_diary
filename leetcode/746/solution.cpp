#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        size_t l = cost.size();
        for (int i = l - 3; i >= 0; i--) {
            cost[i] = min(cost[i + 1], cost[i+2]) + cost[i];
        }        
        return min(cost[0], cost[1]);
    }
};