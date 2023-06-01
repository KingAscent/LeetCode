var createCounter = function(init) {
    let temp = init;
    return{
        increment: () => init += 1,
        decrement: () => init -= 1,
        reset: () => init = temp
    }
};
