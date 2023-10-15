class Solution(object):
    def getDecimalValue(self, head):
        value = 0

        while head:
            value += value
            value += head.val
            head = head.next
        
        return value
