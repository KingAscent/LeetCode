var findNumbers = function(nums) {
    let count = 0;

    nums.forEach(i => {
        let digits = 0;
        while(0 < i){
            digits++;
            i = Math.floor(i / 10);
        }
        if(digits % 2 == 0)
            count++;
    })

    return count;    
};
