class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sum_array = [0 for i in range(len(words))]
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for index, word in enumerate(words):
            # print(index)
            if index > 0:
                prefix_sum_array[index] += prefix_sum_array[index - 1]
            if word[0] in vowels and word[-1] in vowels:
                # print('p')
                prefix_sum_array[index] += 1
        # print(prefix_sum_array)
        output = []
        for query in queries:
            left, right = query  
            ans = prefix_sum_array[right]
            if left > 0:
                ans -= prefix_sum_array[left-1]
            output.append(ans)
        return output


