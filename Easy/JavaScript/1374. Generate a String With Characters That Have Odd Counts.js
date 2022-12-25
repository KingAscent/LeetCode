var generateTheString = function(n) {
    let odd = "";

    for(let i = 0; i < n - 1; i++){
        odd += "a";
    }

    if(n % 2 == 0)
        odd += "b";
    else
        odd += "a";

    return odd;
};
