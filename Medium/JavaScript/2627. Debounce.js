var debounce = function(fn, t) {
    let timer = 0;
    return function(...args) {
        clearTimeout(timer);
        timer = setTimeout(() => fn(...args), t);
    }
};
