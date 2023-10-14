var findClosestNumber = function(nums) {
    let num = 100001;

    for(let i of nums){
        if(Math.abs(i) < Math.abs(num) || i == Math.abs(num))
            num = i;
    }

    return num;
};
