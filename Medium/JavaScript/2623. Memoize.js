function memoize(fn) {
    let k = {};
    return function(...args) {
        let s = String(args);
        if(s in k)
            return k[s];
        let n = fn(...args);
        k[s] = n;
        return n;
    }
}
