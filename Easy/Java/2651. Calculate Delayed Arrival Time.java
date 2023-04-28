class Solution {
    public int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        return (arrivalTime + delayedTime) % 24;

        /*
        Takes less space, but runs slower
        if(24 <= arrivalTime + delayedTime)
            return arrivalTime + delayedTime - 24;
        return arrivalTime + delayedTime;
        */
    }
}
