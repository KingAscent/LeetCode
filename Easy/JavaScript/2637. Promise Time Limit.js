var timeLimit = function(fn, t) {
	return async function(...args) {
        let original = fn(...args);
        let timeOut = new Promise((_, reject) => {
            setTimeout(() => {
                reject('Time Limit Exceeded');
            }, t);
        })

        return Promise.race([original, timeOut]);
    }
};
