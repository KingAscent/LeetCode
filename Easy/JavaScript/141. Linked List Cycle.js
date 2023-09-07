var hasCycle = function(head) {
    fast = head; // Fast pointer
    slow = head; // Slow pointer

    // Loop to see if the fast pointer meets the slow pointer
    while(fast != null && fast.next != null){
        fast = fast.next.next;
        slow = slow.next;
        if(fast == slow)
            return true;
    }

    return false;
};
