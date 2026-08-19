class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size())  return false;
        unordered_map<char, int> freq;
        int l = 0, r = s1.size() - 1;
        for (; r < s2.size(); r++, l++) {
            freq.clear();
            for (char& c: s1)
                freq[c]++;
            for (int i = l; i <= r; i++) {
                if (freq.find(s2[i]) == freq.end())
                    break;
                freq[s2[i]]--;
            }
            int count = 0;
            for (char& c: s1){
                if (freq[c] != 0)
                    break;
                else
                    count++;
                if (count == s1.size())
                    return true;
            }
        }
        return false;
    }
};
