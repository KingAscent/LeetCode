var maxAscendingSum = function(nums) {
    let sum = nums[0];
    let maxSum = sum;

    for(let i = 1; i < nums.length; i++){
        if(nums[i - 1] < nums[i]){
            sum += nums[i];
        }else{
            maxSum = Math.max(maxSum, sum);
            sum = nums[i];
        }
    }
    
    return maxSum < sum ? sum : maxSum;
};
