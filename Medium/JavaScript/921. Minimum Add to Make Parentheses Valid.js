var minAddToMakeValid = function(s) {
    let start = 0;
    let end = 0;

    for(let i = 0; i < s.length; i++){
        if(s.charAt(i) == '('){
            end++;
        }else{
            if(end != 0){
                end--;
            }else{
                start++;
            }
        }
    }

    return start + end;
};
