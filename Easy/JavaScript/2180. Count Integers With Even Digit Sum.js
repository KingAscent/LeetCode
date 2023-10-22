var countEven = function(num) {
    let count = 0;

    for(let i = 2; i <= num; i++){
        let temp = i;
        let sum = 0;
        while(0 < temp){
            sum += Math.floor(temp % 10);
            temp = Math.floor(temp / 10);
        }
        if(sum % 2 == 0)
            count++;
    }

    return count;
};
