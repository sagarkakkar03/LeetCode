
import sys
sys.setrecursionlimit(10**5)
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if abs(i - nums[i]) > 1:
                return False
        return True