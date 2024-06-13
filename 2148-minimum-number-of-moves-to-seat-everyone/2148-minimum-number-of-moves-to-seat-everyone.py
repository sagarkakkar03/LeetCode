class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats.sort()
        students.sort()
        a = 0
        for index in range(len(seats)):
            a += abs(students[index] - seats[index])
        
        return a