var firstMissingPositive = function(nums) {
    let len = nums.length;
    let i = 0;

    while(i < len){
        let temp = nums[i];
        if(1 <= temp && temp <= len){
            if(nums[temp - 1] != temp){
                nums[i] = nums[temp - 1];
                nums[temp - 1] = temp;
            }else{
                i++;
            }
        }else{
            i++;
        }
    }

    for(let j = 0; j < len; j++){
        if(nums[j] != j + 1)
            return j + 1;
    }

    return len + 1;
};
