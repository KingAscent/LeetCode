class Solution {
    public int minOperations(String[] logs) {
        int folder = 0;

        for(String s : logs){
            if(s.charAt(1) == '.')
                folder = Math.max(0, folder - 1);
            else if(s.charAt(0) != '.')
                folder++;
        }

        return folder;
    }
}
