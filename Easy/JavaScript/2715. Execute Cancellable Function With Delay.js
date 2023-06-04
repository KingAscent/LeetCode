var cancellable = function(fn, args, t) {
    let timeOut = setTimeout(() => fn(...args), t);
    return () => clearTimeout(timeOut);
};
