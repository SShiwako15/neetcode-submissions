class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> out;
        for (int i = 0; i < nums.size() - 2; i++) {
            if (nums.at(i) > 0) break;
            if (i > 0 && nums.at(i) == nums[i-1])
                continue;
            int target = nums[i];
            int first = i + 1, last = nums.size() - 1;
            while (first < last) {
                if (target + nums[first] + nums[last] < 0)
                    first++;
                else if (target + nums[first] + nums[last] > 0)
                    last--;
                else {
                    out.push_back({nums[i], nums[first], nums[last]});
                    first++;
                    last--;
                    while (first < last && nums[first] == nums[first-1])
                        first++;
                }
            }

        }
        return out;
    }
};