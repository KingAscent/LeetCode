var findTheDistanceValue = function(arr1, arr2, d) {
    let count = 0;

    for(let i = 0; i < arr1.length; i++){
        let dist = 0;
        for(let j = 0; j < arr2.length; j++){
            let diff = Math.abs(arr1[i] - arr2[j]);
            if(diff <= d)
                j = arr2.length;
            else
                dist++;
        }
        if(dist == arr2.length)
            count++;
    }

    return count;
};
