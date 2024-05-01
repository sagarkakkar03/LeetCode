class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        this = {}
        def find_lcs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in this:
                return this[(i, j)]
            if text1[i] == text2[j]:
                this[(i, j)] = 1 + find_lcs(i+1,j+1)
                return this[(i, j)] 
            this[(i, j)] = max(find_lcs(i+1,j), find_lcs(i, j+1))
            return this[(i, j)]
        return find_lcs(0, 0)