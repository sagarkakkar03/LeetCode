class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        next_smallest = [len(heights) for i in range(len(heights))]
        prev_smallest = [-1 for i in range(len(heights))]
        stack = []
        for i in range(len(heights)):
            while stack and stack[-1][0] > heights[i]:
                curr = stack.pop()
                next_smallest[curr[1]] = i
            stack.append((heights[i], i))
        stack = []
        for i in range(len(heights)-1, -1, -1):
            while stack and stack[-1][0] > heights[i]:
                curr = stack.pop()
                prev_smallest[curr[1]] = i
            stack.append((heights[i], i))
        # print(next_smallest)
        # print(prev_smallest)
        ans = 0
        for i in range(len(heights)):
            # print(i, heights[i]*(i-prev_smallest[i])*(next_smallest[i]-i))
            ans = max(heights[i]*(next_smallest[i]-prev_smallest[i]-1), ans)
        return ans