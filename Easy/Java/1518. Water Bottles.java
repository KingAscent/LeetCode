class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int count = numBottles;

        while(numExchange <= numBottles){
            int temp = numBottles / numExchange;
            count += temp;
            numBottles = temp + (numBottles - (numExchange * temp));
        }

        return count;
    }
}
