var checkString = function(s) {
    found = false;

    for(let i = 0; i < s.length; i++){
        if(s.charAt(i) == 'b')
            found = true;
        if(found && s.charAt(i) == 'a')
            return false;
    }

    return true;
};
