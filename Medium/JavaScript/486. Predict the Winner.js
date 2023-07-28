var PredictTheWinner = function(nums) {
    let n = nums.length;
    let diff = new Array(n).fill(0);

    for(let i = n - 1; 0 <= i; i--){
        diff[i] = nums[i];
        for(let j = i + 1; j < n; j++){
            diff[j] = Math.max(nums[i] - diff[j], nums[j] - diff[j - 1]);
        }
    }

    return 0 <= diff[n - 1];
};
