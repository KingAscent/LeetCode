var canBeEqual = function(target, arr) {
    target.sort((a, b) => a - b);
    arr.sort((a, b) => a - b);
    return target.toString() === arr.toString();
};
