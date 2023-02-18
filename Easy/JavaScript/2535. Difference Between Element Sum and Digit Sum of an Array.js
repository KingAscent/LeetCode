var differenceOfSum = function(nums) {
    let digitSum = 0;
    let arraySum = 0;

    for(let i = 0; i < nums.length; i++){
        arraySum += nums[i];
        while(nums[i] != 0){
            digitSum += nums[i] % 10;
            nums[i] = Math.floor(nums[i] / 10);
        }
    }

    return Math.abs(digitSum - arraySum);
};
