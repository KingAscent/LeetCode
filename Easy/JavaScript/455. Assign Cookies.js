var findContentChildren = function(g, s) {
    let count = 0;
    let i = 0;
    g.sort((a, b) => a - b);
    s.sort((a, b) => a - b);

    for(let j = 0; j < g.length; j++){
        while(i < s.length && s[i] < g[j])
            i++;
        if(i == s.length)
            break;
        i++;
        count++;
    }

    return count;
};
