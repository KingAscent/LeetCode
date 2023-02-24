var alternateDigitSum = function(n) {
    let num = n.toString();
    let sum = 0;

    for(let i = 0; i < num.length; i++){
        if(i % 2 == 0)
            sum += parseInt(num.charAt(i));
        else
            sum -= parseInt(num.charAt(i));
    }

    return sum;
};
