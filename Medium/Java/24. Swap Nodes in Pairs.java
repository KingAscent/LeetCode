class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head == null || head.next == null)
            return head;
        
        ListNode first = head.next;
        head.next = swapPairs(first.next);
        first.next = head;

        return first;
    }
}
