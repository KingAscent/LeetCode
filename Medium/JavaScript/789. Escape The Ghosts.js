var escapeGhosts = function(ghosts, target) {
    let n = Math.abs(target[0]) + Math.abs(target[1]);
    
    for(let ghost of ghosts){
        let dist = Math.abs(target[0] - ghost[0]) + Math.abs(target[1] - ghost[1]);
        if(dist <= n)
            return false;
    }

    return true;
};
