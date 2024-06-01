class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for char in range(len(s)-1):
            ans+=abs(ord(s[char+1]) - ord(s[char]))
        return ans