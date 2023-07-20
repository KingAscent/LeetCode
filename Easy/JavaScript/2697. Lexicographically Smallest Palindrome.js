var makeSmallestPalindrome = function(s) {
    let palin = s.split('');
    let n = s.length;

    for(let i = 0; i < n / 2; i++){
        let j = n - i - 1;
        if(palin[i] != palin[j]){
            if(palin[i] < palin[j])
                palin[j] = palin[i];
            palin[i] = palin[j];
        }
    }

    return palin.join('');
};
