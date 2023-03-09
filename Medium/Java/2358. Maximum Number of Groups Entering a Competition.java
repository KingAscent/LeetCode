class Solution {
    public int maximumGroups(int[] grades) {
        int max = 0;
        int total = 0;
        
        while(max + total + 1 <= grades.length){
            max++;
            total += max;
        }

        return max;
    }
}
