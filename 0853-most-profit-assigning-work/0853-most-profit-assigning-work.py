class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        profit_for_difficulty = [0 for i in range(10**5+1)]
        zipped_arr = sorted(zip(difficulty, profit))
        
        for diff, prof in zipped_arr:
            profit_for_difficulty[diff] = max(profit_for_difficulty[diff], prof)
        
        for i in range(1, 10**5+1):
            profit_for_difficulty[i] = max(profit_for_difficulty[i], profit_for_difficulty[i-1])
        
        ans = 0
        for task in worker:
            ans += profit_for_difficulty[task]
        return ans 