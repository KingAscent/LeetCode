var expect = function(val) {
    return {
        toBe: (val2) => {
            if(val === val2)
                return true;
            else
                throw "Not Equal";
        },

        notToBe: (val2) => {
            if(val !== val2)
                return true;
            else
                throw "Equal";
        }
    }
};
