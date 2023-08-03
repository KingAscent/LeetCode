class Solution {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int count = 0;

        for(int hour : hours){
            if(target <= hour)
                count++;
        }

        return count;
    }
}
