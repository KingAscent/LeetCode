var isAlienSorted = function(words, order) {
    for(let i = 0; i < words.length - 1; i++){
        let w1 = words[i];
        let w2 = words[i + 1];
        if(!isAlienSortedHelper(w1, w2, order))
            return false;
    }

    return true;
};

function isAlienSortedHelper(w1, w2, order){
    if(w1 === w2)
        return true;
    
    let min = Math.min(w1.length, w2.length);
    let j = 0;
    while(j < min && w1.charAt(j) == w2.charAt(j)){
        j++;
    }
    if(j == min){
        return min == w1.length;
    }else{
        let c1 = w1.charAt(j);
        let c2 = w2.charAt(j);
        return order.indexOf(c1) < order.indexOf(c2);
    }
}
