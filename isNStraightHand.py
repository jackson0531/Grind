# given cards, return if cards can be divided into groups with size of groupSize such that every num is consecutive
# use a map to store the frequency 
# sort the maps' keys and start with the smallest available number
# return false early if no number found
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = collections.defaultdict(int)
        for c in hand: 
            freq[c] += 1
        cards = sorted(hand)
        for card in cards: 
            if card not in freq:
                continue
            for c in range(card, card+groupSize): 
                if c not in freq: 
                    return False
                freq[c]-=1
                if freq[c]==0: freq.pop(c)
        return True
