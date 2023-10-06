var intersection = function(nums) {
    let ans = [];
    let count = Array(1001).fill(0);

    for(let i = 0; i < nums.length; i++){
        for(let j = 0; j < nums[i].length; j++){
            count[nums[i][j]]++;
        }
    }

    for(let i = 1; i < 1001; i++){
        if(count[i] == nums.length)
            ans.push(i);
    }

    return ans;
};
