var swapPairs = function(head) {
    if(head == null || head.next == null)
        return head;
    
    let first = head.next;
    head.next = swapPairs(first.next);
    first.next = head;

    return first;
};
