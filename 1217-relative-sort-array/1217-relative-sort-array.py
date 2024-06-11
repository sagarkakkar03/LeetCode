class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = Counter(arr1)
        arr_2 = Counter(arr2)
        output = []
        second = []
        for element in arr_2:
            output += [element]*arr[element]
        for element in arr:
            if element not in arr_2:
                second += [element]*arr[element]
        second.sort()
        output += second 
        return output