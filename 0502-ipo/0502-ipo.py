from heapq import heappush, heappop
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = deque([(profit, capital) for profit, capital in sorted(zip(profits, capital), key = lambda x:x[1])])
        maxHeap = []
        i = 0
        n = len(profits)
        for _ in range(k):
            while i < n and projects[i][1] <= w:
                heappush(maxHeap, -projects[i][0])
                i += 1
            if not maxHeap:
                break 
            w -= heappop(maxHeap)
        return w