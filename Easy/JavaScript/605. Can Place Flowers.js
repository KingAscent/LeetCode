var canPlaceFlowers = function(flowerbed, n) {
    let index = 0;

    while(index < flowerbed.length){
        if(flowerbed[index] == 0 && (index == 0 || flowerbed[index - 1] == 0) &&
          (index == flowerbed.length - 1 || flowerbed[index + 1] == 0)){
              flowerbed[index] = 1;
              n--;
        }
        if(n <= 0)
            return true;
        index++;
    }

    return false;
};
