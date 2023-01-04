var removePalindromeSub = function(s) {
    if(s.length == 0)
        return 0;

    let i = 0;
    let j = s.length - 1;
    
    while(i < j){
        if(s.charAt(i) != s.charAt(j)){
            return 2;
        }else{
            i++;
            j--;
        }
    }

    return 1;    
};
