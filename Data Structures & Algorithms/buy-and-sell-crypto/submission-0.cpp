class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = prices[0];
        int profit = 0;
        for (int i = 1; i < prices.size(); i++) {
            int money = prices[i] - buy;
            profit = max(profit, money);
            buy = min(buy, prices[i]);
        }
        return profit;
    }
};
