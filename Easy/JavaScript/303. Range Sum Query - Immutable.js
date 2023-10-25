let arr;

var NumArray = function(nums) {
    arr = nums;
};

NumArray.prototype.sumRange = function(left, right) {
    let sum = 0;

    for(let i = left; i <= right; i++)
        sum += arr[i];
    
    return sum;
};
