var duplicateZeros = function(arr) {
    let n = arr.length;
    for(let i = 0; i < n; i++){
        if(arr[i] == 0 && i + 1 < n){
            for(let j = n - 1; i + 1 < j; j--)
                arr[j] = arr[j - 1];
            arr[i + 1] = 0;
            i++;
        }
    }
};
