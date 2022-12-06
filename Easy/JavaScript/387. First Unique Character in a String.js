var firstUniqChar = function(s) {
    let map = new Map();

    for(let c of s){
        if(!map.has(c))
            map.set(c, 1);
        else
            map.set(c, map.get(c) + 1);
    }

    for(let i = 0; i < s.length; i++){
        if(map.get(s.charAt(i)) == 1)
            return i;
    }

    return -1;
};
