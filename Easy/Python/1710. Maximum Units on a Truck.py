class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        units = 0

        for box in boxTypes:
            count = min(box[0], truckSize)
            units += count * box[1]
            truckSize -= count
            if truckSize == 0:
                return units

        return units
