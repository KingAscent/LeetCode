var xorAllNums = function(nums1, nums2) {
    if(nums1.length % 2 == 0 && nums2.length % 2 == 0)
        return 0;
    let n = 0;


    if(nums2.length % 2 == 1){
        for(let num of nums1)
            n ^= num;
    }
    if(nums1.length % 2 == 1){
        for(let num of nums2)
            n ^= num;
    }
    
    return n;
};
