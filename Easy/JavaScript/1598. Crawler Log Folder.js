var minOperations = function(logs) {
    let folder = 0;

    for(let s of logs){
        if(s.charAt(1) == '.')
            folder = Math.max(0, folder - 1);
        else if(s.charAt(0) != '.')
            folder++;
    }

    return folder;
};
