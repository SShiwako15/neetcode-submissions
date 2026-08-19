class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 0) return 0;
        unordered_map<char, int> letters;
        int i = 0, length = 0;
        for (int j = 0; j < s.size(); j++) {
            if (letters.find(s[j]) != letters.end())
                i = max(i,letters[s[j]] + 1);
        letters[s[j]] = j;
        length = max(length, j - i + 1);
        }
        return length;
    }
};
