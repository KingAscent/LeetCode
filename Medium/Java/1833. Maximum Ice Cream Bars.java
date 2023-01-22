class Solution {
    public int maxIceCream(int[] costs, int coins) {
        // Counting Sort Algorithm
        // Find the max in the array
        int max = costs[0];
        for(int c : costs){
            max = Math.max(c, max);
        }

        // Find the frequency of each cost
        int[] costFreq = new int[max + 1];
        for(int c : costs){
            costFreq[c]++;
        }

        // Buy the lowest cost ice cream bars to maximize
        // amount of ice cream bars purchased
        int count = 0;
        for(int i = 1; i <= max; i++){
            int freq = costFreq[i];
            if(coins < i){
                break;
            }
            int buy = Math.min(freq, coins / i);
            coins -= i * buy;
            count += buy;
        }

        return count;
    }
}

/*
    // Greedy Sort
    public int maxIceCream(int[] costs, int coins) {
        Arrays.sort(costs);
        int count = 0;
        int index = 0;

        while(0 < coins && index < costs.length){
            if(costs[index] <= coins){
                coins -= costs[index];
                count++;
            }
            if(coins < costs[index])
                coins = 0;
            index++;
        }

        return count;
    }
*/
