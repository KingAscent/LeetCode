var minInsertions = function(s) {
    let n = s.length;
    let min = new Array(n).fill(0);

    for(let i = n - 1; 0 <= i; i--){
        let prev = 0;
        for(let j = i; j < n; j++){
            let temp = min[j];
            if(s.charAt(i) == s.charAt(j))
                min[j] = prev;
            else
                min[j] = Math.min(min[j], min[j - 1]) + 1;
            prev = temp;
        }
    }

    return min[n - 1];
};
