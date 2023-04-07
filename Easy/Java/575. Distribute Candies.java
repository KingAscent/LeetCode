class Solution {
    public int distributeCandies(int[] candyType) {
        Arrays.sort(candyType);
        int len = candyType.length;
        int count = 0;
        int limit = len / 2;

        for(int i = 0; i < len && 0 < limit; i++){
            while(i < len - 1 && candyType[i] == candyType[i + 1]){
                i++;
            }
            count++;
            limit--;
        }

        return count;
    }
}
