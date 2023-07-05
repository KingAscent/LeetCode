var findMatrix = function(nums) {
    let set = [];

    nums.forEach((n) => {
        let i = 0;
        while(i < set.length && set[i].has(n)){
            i++;
        }
        if(i === set.length)
            set.push(new Set([n]));
        else
            set[i].add(n);
    })

    for(let i in set){
        set[i] = Array.from(set[i]);
    }

    return set;
};
