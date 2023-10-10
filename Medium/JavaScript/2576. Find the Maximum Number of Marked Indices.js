var maxNumOfMarkedIndices = function(nums) {
    let i = 0;
    let j = Math.floor((nums.length + 1) / 2);
    nums.sort((a, b) => a - b);

    while(j < nums.length){
        if(2 * nums[i] <= nums[j])
            i++;
        j++;
    }

    return 2 * i;
};
