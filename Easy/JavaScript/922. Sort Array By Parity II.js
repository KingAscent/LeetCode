var sortArrayByParityII = function(nums) {
    let parity = Array(nums.length);
    let even = 0;
    let odd = 1;

    for(let i = 0; i < nums.length; i++){
        if(nums[i] % 2 == 0){
            parity[even] = nums[i];
            even += 2;
        }else{
            parity[odd] = nums[i];
            odd += 2;
        }
    }

    return parity;
};
