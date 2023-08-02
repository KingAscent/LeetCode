var validMountainArray = function(arr) {
    let n = arr.length;
    if(n < 3)
        return false;
    let l = 0;
    let r = n - 1;

    // Double pointers
    while(l < n - 2 && arr[l] < arr[l + 1]){
        l++;
    }
    while(1 < r && arr[r] < arr[r - 1]){
        r--;
    }

    return l == r;
};
