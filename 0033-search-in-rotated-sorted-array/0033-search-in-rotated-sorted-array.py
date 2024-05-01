class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+ right)//2
            print(left, right, nums[mid])
            if nums[mid] == target:
                return mid
            # identify sorted half
            if nums[mid] >= nums[left]:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    if target >= nums[left]:
                        right = mid -1
                    else:
                        left = mid + 1
            else:
                if nums[mid] > target:
                    right = mid - 1
                else:
                    if target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1