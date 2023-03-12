var removeStars = function(s) {
    let starless = [];

    for(let c of s){
        if(c != '*')
            starless.push(c);
        else
            starless.pop();
    }

    return starless.join("");
};
