class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        ans = float('inf')
        index = -1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < ans:
                index = mid
                ans = nums[mid]
            if nums[mid] < nums[right]: 
                right = mid - 1
            else:
                left = mid+1
        return ans