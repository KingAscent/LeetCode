class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        int zeros = 0;
        int ones = 0;

        for(int n : students){
            if(n == 0)
                zeros++;
            else
                ones++;
        }

        for(int n : sandwiches){
            if((n == 0 && zeros == 0) || (n == 1 && ones == 0))
                break;
            if(n == 0)
                zeros--;
            else
                ones--;
        }

        return Math.max(zeros, ones);
    }
}
