var peakIndexInMountainArray = function(arr) {
    let left = 0;
    let right = arr.length - 1;

    while(left < right){
        let temp = Math.floor((left + right) / 2);
        if(arr[temp] < arr[temp + 1])
            left = temp + 1;
        else
            right = temp;
    }

    return left;
};
