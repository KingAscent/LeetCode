var pivotIndex = function(nums) {
    let pivot = -1;
    let left = 0;
    let total = 0;

    for(let n of nums)
        total += n;
    
    for(let i = 0; i < nums.length; i++){
        if(left * 2 == total - nums[i]){
            pivot = i;
            break;
        }else{
            left += nums[i];
        }
    }

    return pivot;
};
