class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> output;
        for (string s: strs){
            vector<int> binary(26, 0);
            for (char c: s)
                binary[c - 'a']++;
            string key = to_string(binary[0]);
            for (int i = 1; i < 26; i++)
                key += ',' + to_string(binary[i]);
            output[key].push_back(s);
        }
        vector<vector<string>> result;
        for (const auto& pair: output)
            result.push_back(pair.second);
        return result;
    }
};
