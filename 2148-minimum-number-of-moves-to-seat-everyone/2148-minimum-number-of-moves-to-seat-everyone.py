class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats.sort()
        students.sort()
        ans = 0
        for index in range(len(seats)):
            ans += abs(students[index] - seats[index])
        
        return ans