var flipAndInvertImage = function(image) {
    image.forEach(col =>{
        let i = 0;
        let j = image.length - 1;

        while(i <= j){
            let temp = col[i];
            col[i++] = 1 - col[j];
            col[j--] = 1 - temp;
        }
    })

    return image;
};
