var pivotArray = function(nums, pivot) {
    let len = nums.length;
    let rearranged = Array(len).fill(0);
    let index = 0;

    for(let i = 0; i < len; i++){
        if(nums[i] < pivot){
            rearranged[index] = nums[i];
            index++;
        }
    }

    for(let i = 0; i < len; i++){
        if(nums[i] == pivot){
            rearranged[index] = nums[i];
            index++;
        }
    }

    for(let i = 0; i < len; i++){
        if(pivot < nums[i]){
            rearranged[index] = nums[i];
            index++;
        }
    }

    return rearranged;
};
