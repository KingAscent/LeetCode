class Solution(object):
    def isWinner(self, player1, player2):
        p1 = 0
        p2 = 0
        
        for i in range(len(player1)):
            if ((i == 1 and player1[i - 1] == 10) or
                (2 <= i and (player1[i - 1] == 10 or player1[i - 2] == 10))):
                p1 += player1[i]
            
            if ((i == 1 and player2[i - 1] == 10) or
                (2 <= i and (player2[i - 1] == 10 or player2[i - 2] == 10))):
                p2 += player2[i]
            
            p1 += player1[i]
            p2 += player2[i]
        
        return 1 if p2 < p1 else 2 if p1 < p2 else 0
