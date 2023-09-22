var finalString = function(s) {
    let sb = [];

    for(let c of s){
        if(c == 'i')
            sb.reverse();
        else
            sb.push(c);
    }

    return sb.join("");
};
