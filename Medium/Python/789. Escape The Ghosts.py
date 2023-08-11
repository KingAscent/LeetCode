class Solution(object):
    def escapeGhosts(self, ghosts, target):
        n = abs(target[0]) + abs(target[1])

        for ghost in ghosts:
            dist = abs(target[0] - ghost[0]) + abs(target[1] - ghost[1])
            if dist <= n:
                return False
        
        return True
