var minPartitions = function(n) {
    let db = 0;

    for(let i = 0; i < n.length; i++){
        db = Math.max(db, n.charAt(i) - '0');
    }

    return db;
};
