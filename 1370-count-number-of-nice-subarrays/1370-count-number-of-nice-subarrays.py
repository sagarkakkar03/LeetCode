class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        sub_sum = {0 : 1}
        sumi = 0
        count = 0
        for curr_num in nums:
            if curr_num %2:
                num = 1
            else:
                num = 0
            sumi += num
            if sumi - k in sub_sum:
                count += sub_sum[sumi - k]
            if sumi not in sub_sum:
                sub_sum[sumi] = 0
            sub_sum[sumi] += 1
        return count