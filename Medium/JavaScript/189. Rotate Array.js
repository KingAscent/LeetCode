var rotate = function(nums, k) {
    // In the event k is larger than nums.length,
    // simplify so to not rotate in circles
    let n = nums.length;
    k %= n;
    let temp = Array(n).fill(0);

    for(let i = 0; i < n; i++){
        temp[(i + k) % n] = nums[i];
    }

    for(let i = 0; i < n; i++){
        nums[i] = temp[i];
    }
};
