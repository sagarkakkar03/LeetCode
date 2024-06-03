class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        return len(t) - self.lcs(0, 0, s, t)        
    def lcs(self, index_s, index_t, s, t):
        if index_s == len(s) or index_t == len(t):
            return 0
        if s[index_s] == t[index_t]:
            return 1 + self.lcs(index_s+1, index_t+1, s, t)
        return self.lcs(index_s+1, index_t, s, t)