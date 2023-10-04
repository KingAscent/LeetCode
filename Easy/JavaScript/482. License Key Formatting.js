var licenseKeyFormatting = function(s, k) {
    let license = [];

    for(let i = s.length - 1; 0 <= i; i--){
        if(s.charAt(i) != '-'){
            if(license.length % (k + 1) == k)
                license.push('-');
            license.push(s.charAt(i));
        }
    }

    return license.reverse().join("").toUpperCase();
};
