class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> lfreq;
        int l = 0;
        int maxFreq = 0, length = 0;
        for (int r = 0; r < s.size(); r++)
        {
            lfreq[s[r]] += 1;
            maxFreq = max(maxFreq, lfreq[s[r]]);
            while ( (r - l + 1) - maxFreq > k) {
                lfreq[s[l]]--;
                l++;
            }
            length = max((r - l + 1), length);
        }
        return length;
    }
};