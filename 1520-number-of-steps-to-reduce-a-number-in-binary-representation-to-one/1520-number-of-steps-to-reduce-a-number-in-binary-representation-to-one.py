class Solution:
    def numSteps(self, s: str) -> int:
        carry = steps = 0
        for curr in s[1:len(s)][::-1]:
            val = carry
            if curr == '1':
                if carry:
                    steps += 1
                else:
                    steps += 2
                carry = 1
            else:
                if carry:
                    steps +=2
                    carry = 1
                else:
                    steps += 1
                    carry = 0
        if s[0] =='1' and carry == 1:
            steps +=1
        return steps