class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        height_counter = Counter(heights)
        height_sorted = list(height_counter.keys())
        height_sorted.sort()
        index = 0 
        output = 0
        for height in height_sorted:
            height_count = height_counter[height]
            while height_count:
                height_count -= 1
                if heights[index] != height:
                    output += 1
                index += 1
        return output