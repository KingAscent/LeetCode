var dominantIndex = function(nums) {
    let largest = 0;        // Index of largest element
    let secondLargest = 1;  // Index of second largest element

    for(let i = 1; i < nums.length; i++){
        if(nums[largest] < nums[i]){
            secondLargest = largest;
            largest = i;
        }else if(nums[secondLargest] < nums[i])
            secondLargest = i;
    }

    return nums[secondLargest] * 2 <= nums[largest] ? largest : -1;
};
