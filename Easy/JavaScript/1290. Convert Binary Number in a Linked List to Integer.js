var getDecimalValue = function(head) {
    let value = 0;

    while(head != null){
        value += value;
        value += head.val;
        head = head.next;
    }

    return value;
};
