var searchRange = function(nums, target) {
    // Find the first appearance of the target
    let first = findFirst(nums, 0, target);

    // Find the last appearance of the target, and return an array
    // containing the first and last appearance indeces
    return [first, findLast(nums, nums.length - 1, target)];
};

var findFirst = function(nums, i, target) {
    while(i < nums.length){
        if(nums[i] == target)
            return i;
        else
            i++;
    }

    // Target wasn't found, so return -1
    return -1;
}

var findLast = function(nums, j, target) {
    while(0 <= j){
        if(nums[j] == target)
            return j;
        else
            j--;
    }

    // Target wasn't found, so return -1
    return -1;
}
