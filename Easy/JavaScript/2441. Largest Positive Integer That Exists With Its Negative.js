var findMaxK = function(nums) {
    nums.sort((a, b) => a - b);
    let start = 0;
    let end = nums.length - 1;
    let max = -1;
    if(0 < nums[start])
        return max;
    
    while(start < end){
        if(nums[start] + nums[end] == 0){
            max = nums[end];
            break;
        }else if(Math.abs(nums[start]) < nums[end]){
            end--;
        }else{
            start++;
        }
    }

    return max;
};
