class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        len_pref = len(pref)
        result = 0
        for word in words:
            if len(word) >= len_pref and pref == word[:len_pref]:
                result += 1
        return result 