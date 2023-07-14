Function.prototype.callPolyfill = function(context, ...args) {
    let unique = Symbol();
    context[unique] = this;
    let res = context[unique](...args);
    delete context[unique];
    return res;
}
