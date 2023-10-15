class Solution {
    public int getDecimalValue(ListNode head) {
        int value = 0;

        while(head != null){
            value += value;
            value += head.val;
            head = head.next;
        }

        return value;
    }
}
