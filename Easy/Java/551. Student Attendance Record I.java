class Solution {
    public boolean checkRecord(String s) {
        int countAbsent = 0;

        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == 'A')
                countAbsent++;
            if(i < s.length() - 2 && s.substring(i, i + 3).equals("LLL"))
                return false;
        }

        return countAbsent < 2;
    }
}
