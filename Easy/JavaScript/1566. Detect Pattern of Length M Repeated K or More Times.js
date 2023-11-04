var containsPattern = function(arr, m, k) {
    let count = 0;

    for(let i = 0; i < arr.length - m; i++){
        count = (arr[i] == arr[i + m] ? count + 1 : 0);
        if(count == m * (k - 1))
            return true;
    }

    return false;
};
