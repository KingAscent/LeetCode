var numberOfArithmeticSlices = function(nums) {
    let slices = 0;
    let prev = 0;

    for(let i = 2; i < nums.length; i++){
        if(nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]){
            prev += 1;
            slices += prev;
        }else{
            prev = 0;
        }
    }

    return slices;
};
