class Solution {
    public int partitionString(String s) {
        int start = 0;
        int end = 0;
        int count = 0;

        while(end < s.length()){
            if(s.substring(start, end).contains(s.charAt(end) + "")){
                count++;
                start = end;
            }
            end++;
        }

        if(s.substring(start, end).contains(s.charAt(end - 1) + "")){
            count++;
        }

        return count;
    }
}
