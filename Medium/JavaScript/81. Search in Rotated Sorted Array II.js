var search = function(nums, target) {
    let start = 0;
    let end = nums.length - 1;

    while(start <= end){
        let mid = start + Math.floor((end - start) / 2);
        if(nums[mid] == target)
            return true;
        
        // Handle duplicates
        if(nums[start] == nums[mid] && nums[mid] == nums[end]){
            start++;
            end--;
        }

        // Sorted left half
        else if(nums[start] <= nums[mid]){
            if(nums[start] <= target && target <= nums[mid])
                end = mid - 1;
            else
                start = mid + 1;
        }

        // Sorted right half
        else{
            if(nums[mid] <= target && target <= nums[end])
                start = mid + 1;
            else
                end = mid - 1;
        }
    }

    return false;
};
