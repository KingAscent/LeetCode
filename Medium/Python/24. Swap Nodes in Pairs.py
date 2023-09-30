class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        
        first = head.next
        head.next = self.swapPairs(first.next)
        first.next = head

        return first
