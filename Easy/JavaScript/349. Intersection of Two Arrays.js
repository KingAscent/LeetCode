var intersection = function(nums1, nums2) {
    let freq = new Set();

    for(let i = 0; i < nums1.length; i++){
        for(let j = 0; j < nums2.length; j++){
            if(nums1[i] == nums2[j] && !freq.has(nums1[i])){
                freq.add(nums1[i]);
                break;
            }
        }
    }

    let count = Array(freq.size).fill(0);
    let index = 0;
    for(let n of freq){
        count[index] = n;
        index++;
    }

    return count;
};
