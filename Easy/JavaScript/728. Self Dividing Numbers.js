var selfDividingNumbers = function(left, right) {
    var list = [];

    for(let i = left; i <= right; i++){
        let number = i;
        while(0 < number){
            if((number % 10) != 0 && i % (number % 10) == 0)
                number = Math.floor(number / 10);
            else
                number = -1;
        }
        if(number != -1)
            list.push(i);
    }
    
    return list;
};
