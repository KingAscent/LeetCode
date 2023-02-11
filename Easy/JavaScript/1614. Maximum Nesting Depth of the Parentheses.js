var maxDepth = function(s) {
    let depth = 0;
    let open = 0;

    for(let i = 0; i < s.length; i++){
        if(s.charAt(i) == '('){
            open++;
            depth = Math.max(depth, open);
        }
        if(s.charAt(i) == ')')
            open--;
    }

    return depth;
};
