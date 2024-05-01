import sys
sys.setrecursionlimit(10**5)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def recursion(i, sumi, arr):
            if i >= len(candidates) or sumi > target:
                return 
            if sumi == target:
                ans.append(arr.copy())
                return 
            recursion(i, sumi + candidates[i], arr + [candidates[i]])
            recursion(i+1, sumi, arr)
        recursion(0, 0, [])
        return ans 