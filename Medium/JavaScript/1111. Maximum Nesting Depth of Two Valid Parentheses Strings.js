var maxDepthAfterSplit = function(seq) {
    let par = Array(seq.length).fill(0);
    let count = 0;

    for(let i = 0; i < seq.length; i++){
        if(seq.charAt(i) == '('){
            count++;
            par[i] = count % 2;
        }else{
            par[i] = count % 2;
            count--;
        }
    }

    return par;
};
