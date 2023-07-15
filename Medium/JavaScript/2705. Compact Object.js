var compactObject = function(obj) {
    if(!obj)
        return null;
    if(Array.isArray(obj))
        return obj.filter(Boolean).map(compactObject);
    if(typeof obj !== "object")
        return obj;
    
    let comp = {};
    for(let index in obj){
        let val = compactObject(obj[index]);
        if(Boolean(val))
            comp[index] = val
    }

    return comp;
};
