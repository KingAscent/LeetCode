class Solution(object):
    def reverseList(self, head):
        prev = None
        nextHead = None

        while head:
            nextHead = head.next
            head.next = prev
            prev = head
            head = nextHead
        
        return prev
