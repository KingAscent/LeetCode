var nextGreaterElement = function(nums1, nums2) {
    let ans = Array(nums1.length).fill(0);

    for(let i = 0; i < nums1.length; i++){
        let found = false;
        for(let j = 0; j < nums2.length; j++){
            if(nums1[i] == nums2[j])
                found = true;
            if(found && nums1[i] < nums2[j]){
                ans[i] = nums2[j];
                break;
            }
        }
        if(ans[i] == 0)
            ans[i]--;
    }

    return ans;
};
