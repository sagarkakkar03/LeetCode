class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True

        number_of_cards = len(hand) 
        if number_of_cards%groupSize:
            return False 
        hand.sort()
        hand_bool = [True for i in range(number_of_cards)]
        for i in range(number_of_cards):
            curr = hand[i]
            count = 1
            if hand_bool[i]:
                hand_bool[i] = False
                for j in range(i+1, number_of_cards):
                    if hand_bool[j] and curr + 1 == hand[j] and count < groupSize:
                        count += 1
                        hand_bool[j] = False
                        curr = hand[j]
                if count != groupSize:
                    return False

        return True
                
