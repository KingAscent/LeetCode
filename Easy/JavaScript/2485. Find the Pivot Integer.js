var pivotInteger = function(n) {
    let pivot = -1;
    let left = 0;

    for(let i = 0; i <= n; i++){
        left += i;
        let right = 0;

        for(let j = i; j <= n; j++)
            right += j;
        
        if(left == right)
            pivot = i;
    }

    return pivot;
};
