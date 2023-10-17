var countSeniors = function(details) {
    let count = 0;

    for(s of details){
        if(parseInt(s.substring(11, 13)) > 60)
            count++;
    }

    return count;
};
