class Solution {
    public int numberOfSteps(int num) {
        int count = 0;
        while(0 < num){
            if(num % 2 == 0)
                num /= 2;
            else
                num -= 1;
            count++;
        }
        return count;
    }
}
