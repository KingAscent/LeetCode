var strStr = function(haystack, needle) {
    let left = 0;
    let right = needle.length - 1;

    while(right < haystack.length){
        let temp = haystack.substring(left, right + 1);
        if(temp == needle)
            return left;
        left++;
        right++;
    }

    return -1;
};
