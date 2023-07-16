var promiseAll = async function(functions) {
    return new Promise((resolve, reject) => {
        let ans = new Array(functions.length);
        let count = functions.length;

        for(let i = 0; i < functions.length; i++){
            let func = functions[i];
            func()
                .then((n) => {
                    ans[i] = n;
                    count--;
                    if(count === 0)
                        return resolve(ans);
                })
                .catch(reject);
        }
    })
};
