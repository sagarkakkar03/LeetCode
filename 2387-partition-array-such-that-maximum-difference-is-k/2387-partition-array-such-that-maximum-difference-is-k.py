class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        mini = nums[0]
        maxi = nums[0]
        count = 1
        for num in nums:
            if abs(mini - num) > k or abs(maxi - num) > k:
                maxi = mini = num 
                count += 1
        return count
