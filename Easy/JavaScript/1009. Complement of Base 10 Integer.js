var bitwiseComplement = function(n) {
    let complement = 1;

    while(complement < n)
        complement = complement * 2 + 1;
    
    return complement - n;
};
