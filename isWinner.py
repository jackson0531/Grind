class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        A, B = 0, 0
        for i in range(len(player1)): 
            # A 
            A += player1[i]
            if (i-1>=0 and player1[i-1]==10) or (i-2>=0 and player1[i-2]==10): 
                A+= player1[i]
            # B 
            B += player2[i]
            if (i-1>=0 and player2[i-1]==10) or (i-2>=0 and player2[i-2]==10): 
                B+= player2[i]
        if A>B: return 1
        elif A<B: return 2
        else: return 0
