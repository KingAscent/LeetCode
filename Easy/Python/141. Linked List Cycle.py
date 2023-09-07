class Solution(object):
    def hasCycle(self, head):
        fast = head # Fast pointer
        slow = head # Slow pointer

        # Loop to see if the fast pointer meets the slow pointer
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False
