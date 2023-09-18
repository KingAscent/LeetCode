var findKthPositive = function(arr, k) {
    for(let n of arr){
        if(n <= k)
            k++;
        else
            break;
    }

    return k;
};
