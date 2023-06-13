class Solution {
    public int numberOfBeams(String[] bank) {
        int count = 0;
        int prev = 0;

        for(String s : bank){
            int temp = 0;
            for(int i = 0; i < s.length(); i++){
                if(s.charAt(i) == '1')
                    temp++;
            }
            count += prev * temp;
            if(0 < temp)
                prev = temp;
        }

        return count;
    }
}
