class Solution:
    def longestPalindrome(self, s: str) -> int:
        alphabet_dictionary = Counter(s)
        odd = 0
        ans = 0
        for alphabet_in_alphabet_dictionary in alphabet_dictionary:
            if alphabet_dictionary[alphabet_in_alphabet_dictionary] %2 == 0:
                ans += alphabet_dictionary[alphabet_in_alphabet_dictionary]
            else:
                ans += alphabet_dictionary[alphabet_in_alphabet_dictionary] - 1
                odd = 1
        return ans + odd 
