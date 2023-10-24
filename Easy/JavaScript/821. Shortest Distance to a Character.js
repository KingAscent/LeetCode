var shortestToChar = function(s, c) {
    let len = s.length;
    let dist = Array(len).fill(len);

    for(let i = 0; i < len; i++){
        if(s.charAt(i) == c){
            for(let j = 0; j < len; j++){
                dist[j] = Math.min(dist[j], Math.abs(i - j));
            }
        }
    }

    return dist;
};
