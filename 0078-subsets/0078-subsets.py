class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2**len(nums)):
            temp = i
            temp_ans = []
            j = 0
            while temp>>j:
                if (temp>>j)&1:
                    temp_ans.append(nums[j])
                j+=1
            ans.append(temp_ans)
        return ans
