var countDigits = function(num) {
    let count = 0;
    let temp = num;

    while(temp != 0){
        if(Math.floor(temp % 10) != 0 && Math.floor(num % Math.floor(temp % 10)) == 0)
            count++;
        temp /= 10;
    }

    return count;
};
