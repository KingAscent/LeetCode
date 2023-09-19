var threeConsecutiveOdds = function(arr) {
    for(let i = 0; i < arr.length - 2; i++){
        let odd1 = arr[i] % 2 == 1;
        let odd2 = arr[i + 1] % 2 == 1;
        let odd3 = arr[i + 2] % 2 == 1;
        if(odd1 && odd2 && odd3)
            return true;
    }

    return false;
};
