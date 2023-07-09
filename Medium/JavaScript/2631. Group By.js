Array.prototype.groupBy = function(fn) {
    let group = {};
    let len = this.length;
    
    for(let i = 0; i < len; i++){
        let id = fn(this[i]);
        if(group[id] === undefined)
                group[id] = [];
        group[id].push(this[i]);
    }
    
    return group;
};
