var cancellable = function(fn, args, t) {
    fn(...args);
    let valid = setInterval(() => fn(...args), t);
    return () => clearInterval(valid);
};
