var minDeletion = function(nums) {
    let del = 0;

    for(let i = 0; i < nums.length - 1; i += 2){
        if(nums[i] == nums[i + 1]){
            del++;
            i--;
        }
    }

    if((nums.length - del) % 2 == 0)
        return del;
    return del + 1;
};
