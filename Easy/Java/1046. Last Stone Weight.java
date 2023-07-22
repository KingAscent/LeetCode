class Solution {
    public int lastStoneWeight(int[] stones) {
        Arrays.sort(stones);
        int n = stones.length;
        if(n == 1)
            return stones[0];
        

        while(0 < stones[n - 2]){
            int temp = stones[n - 1] - stones[n - 2];
            stones[n - 2] = 0;
            stones[n - 1] = temp;
            Arrays.sort(stones);
        }

        return stones[n - 1];
    }
}
