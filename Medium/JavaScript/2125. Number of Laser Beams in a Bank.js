var numberOfBeams = function(bank) {
    let count = 0;
    let prev = 0;

    bank.forEach((s) => {
        let temp = 0;
        for(let i = 0; i < s.length; i++){
            if(s.charAt(i) == '1')
                temp++;
        }
        count += prev * temp;
        if(0 < temp)
            prev = temp;
    })

    return count;
};
