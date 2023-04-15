var compose = function(functions) {
	return function(x) {
        let fn = x;

        for(let i = functions.length - 1; 0 <= i; i--){
            fn = functions[i](fn);
        }

        return fn;
    }
};
