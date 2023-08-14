var unequalTriplets = function(nums) {
    let count = 0;
    let n = nums.length;

    for(let i = 0; i < n - 2; i++){
        let a = nums[i];
        for(let j = i + 1; j < n - 1; j++){
            let b = nums[j];
            for(let k = i + 2; k < n; k++){
                let c = nums[k];
                if(i < j && j < k){
                    if(a != b && b != c && a != c)
                        count++;
                }
            }
        }
    }

    return count;
};
