var largestOddNumber = function(num) {
    let i = num.length - 1;

    while(0 <= i){
        if(num.charAt(i) % 2 == 1)
            return num.substring(0, i + 1);
        i -= 1;
    }

    return "";
};
