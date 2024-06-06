class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True

        number_of_cards = len(hand) 
        if number_of_cards%groupSize:
            return False 

        c = Counter(hand)
        for i in sorted(hand):
            # print(c, i)
            if c[i] > 0:
                val = c[i]
                for j in range(groupSize):
                    if i+j in c:
                        # print(i,i+j)
                        c[i+j] -= val
                    else:
                        return False
                    if c[i+j] < 0:
                        return False

        # print(c)
        return True
                
