class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count, ans = 0, 0
        string = set()
        l = 0
        for i in range(len(s)):
            if s[i] in string:
                while s[l]!=s[i]:
                    string.remove(s[l])
                    l += 1
                string.remove(s[l])
                l += 1
            string.add(s[i])
            ans = max(ans, len(string))
        return ans
                
        