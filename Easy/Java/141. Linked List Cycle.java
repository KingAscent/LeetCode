public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode fast = head; // Fast pointer
        ListNode slow = head; // Slow pointer

        // Loop to see if the fast pointer meets the slow pointer
        while(fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
            if(fast == slow)
                return true;
        }

        return false;
    }
}
