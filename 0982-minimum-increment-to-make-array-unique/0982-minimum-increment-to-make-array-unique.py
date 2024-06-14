class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev >= nums[i]:
                ans += (prev-nums[i]+1)
                prev = prev + 1
            else:
                prev = nums[i]
        return ans