var validateStackSequences = function(pushed, popped) {
    let stack = [];
    let i = 0;

    for(let n of pushed){
        stack.push(n);
        while(0 < stack.length && stack[stack.length - 1] === popped[i]){
            stack.pop();
            i++;
        }
    }

    return i === popped.length;
};
