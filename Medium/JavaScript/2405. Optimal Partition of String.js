var partitionString = function(s) {
    let start = 0;
    let end = 0;
    let count = 0;

    while(start < s.length){
        if(s.substring(start, end).includes(s.charAt(end) + "")){
            count++;
            start = end;
        }
        end++;
    }

    return count;
};
