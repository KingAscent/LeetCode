class Solution {
    public int balancedStringSplit(String s) {
        int countR = 0;
        int countL = 0;
        int count = 0;

        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == 'L')
                countL++;
            else
                countR++;
            if(countR == countL && countR != 0){
                count++;
                countL = 0;
                countR = 0;
            }
        }
        
        return count;
    }
}
