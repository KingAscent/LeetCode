var removeDuplicates = function(nums) {
    if(nums.length < 3)
        return nums.length;
    
    let i = 2;
    for(let j = i; j < nums.length; j++){
        if(nums[i - 2] != nums[j]){
            nums[i] = nums[j];
            i++;
        }
    }

    return i;
};
