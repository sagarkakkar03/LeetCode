class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        place_zero = 0
        place_two = len(nums) - 1
        index = 0
        while index < len(nums) and index <= place_two:
            if nums[index] == 0 :
                nums[place_zero], nums[index] = nums[index], nums[place_zero]
                place_zero += 1
                index += 1
            elif nums[index] == 2 :
                nums[place_two], nums[index] = nums[index], nums[place_two]
                place_two -= 1
            else:
                index += 1
            
            
