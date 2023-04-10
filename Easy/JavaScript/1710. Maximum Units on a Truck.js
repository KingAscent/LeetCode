var maximumUnits = function(boxTypes, truckSize) {
    boxTypes.sort((a, b) => b[1] - a[1]);
    let units = 0;

    boxTypes.forEach((box) => {
        let count = Math.min(box[0], truckSize);
        units += count * box[1];
        truckSize -= count;
        if(truckSize == 0)
            return units;
    })

    return units;
};
