var findMedianSortedArrays = function(nums1, nums2) {
    // Create a new array
    merged = Array(nums1.length + nums2.length).fill(0);

    // Use a while loop to add values from nums1 and nums2 to the new array
    let i = 0;
    let j = 0;
    while(i < nums1.length || j < nums2.length){
        if(i < nums1.length){
            merged[i] = nums1[i];
            i++;
        }
        if(j < nums2.length){
            merged[j + nums1.length] = nums2[j];
            j++;
        }
    }

    // Sort the array without the sort function (Bubble Sort)
    for(let m = 0; m < merged.length; m++){
        for(let n = m + 1; n < merged.length; n++){
            let temp = 0;
            if(merged[n] < merged[m]){
                temp = merged[m];
                merged[m] = merged[n];
                merged[n] = temp;
            }
        }
    }

    // Find the median double, and return it
    let middle = Math.floor(merged.length / 2);
    if(merged.length % 2 != 0)
        return merged[middle];
    else
        return (merged[middle] + merged[middle - 1]) / 2;
};
