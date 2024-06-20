class Solution:
    def __init__(self):
        self.position = None
        self.m = None 
    def check_answer(self, possible_answer):
        prev = float('-inf')
        value = self.m
        for index, pos in enumerate(self.position):
            if pos - prev >= possible_answer:
                value -= 1
                prev = pos 
        return True if value <= 0 else False

    def binary_search_on_answer(self):
        left, right = 0, 999999999999999999999
        while left <= right:
            mid = (left+right)//2
            if self.check_answer(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        self.position = position
        self.m = m 
        return self.binary_search_on_answer()