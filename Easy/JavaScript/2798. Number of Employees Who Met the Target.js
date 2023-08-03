var numberOfEmployeesWhoMetTarget = function(hours, target) {
    let count = 0;

    for(let hour of hours){
        if(target <= hour)
            count++;
    }

    return count;
};
