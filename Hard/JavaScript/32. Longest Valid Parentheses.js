var longestValidParentheses = function(s) {
    let open = 0;
    let close = 0;
    let longest = 0;

    for(let i = 0; i < s.length; i++){
        if(s.charAt(i) == '('){
            open++;
        }else{
            close++;
        }

        if(open == close){
            longest = Math.max(longest, 2 * close);
        }else if(open <= close){
            open = 0;
            close = 0;
        }
    }

    open = 0;
    close = 0;

    for(let i = s.length - 1; 0 <= i; i--){
        if(s.charAt(i) == '('){
            open++;
        }else{
            close++;
        }

        if(open == close){
            longest = Math.max(longest, 2 * open);
        }else if(close <= open){
            open = 0;
            close = 0;
        }
    }

    return longest;
};
