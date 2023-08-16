var wiggleSort = function(nums) {
    nums.sort((a, b) => a - b);
    let mid = Math.floor((nums.length - 1) / 2);
    let end = nums.length - 1;
    let store = Array(end + 1).fill(0);
    let count = 0;
    
    while(0 <= mid || Math.floor((nums.length - 1) / 2) < end){
        if(count % 2 == 0){
            store[count] = nums[mid];
            mid--;
        }else{
            store[count] = nums[end];
            end--;
        }
        count++;
    }

    for(let i = 0; i < nums.length; i++){
        nums[i] = store[i];
    }
};
