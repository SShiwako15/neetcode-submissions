class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0, right = heights.size() - 1;
        int max_water = INT_MIN;
        while (left < right) {
            int water = (right-left) * min(heights[left], heights[right]);
            max_water = max(max_water, water);
            (heights[left] > heights[right]) ? right-- : left++;
        }
        return max_water;
    }
};
