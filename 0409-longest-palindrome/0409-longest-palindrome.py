class Solution:
    def longestPalindrome(self, s: str) -> int:
        alphabet_dictionary = {}
        for alphabet_in_s in s:
            if alphabet_in_s not in alphabet_dictionary:
                alphabet_dictionary[alphabet_in_s] = 0
            alphabet_dictionary[alphabet_in_s] += 1
        odd = 0
        ans = 0
        for alphabet_in_alphabet_dictionary in alphabet_dictionary:
            if alphabet_dictionary[alphabet_in_alphabet_dictionary] %2 == 0:
                ans += alphabet_dictionary[alphabet_in_alphabet_dictionary]
            else:
                ans += alphabet_dictionary[alphabet_in_alphabet_dictionary] - 1
                odd = 1
        return ans + odd 
