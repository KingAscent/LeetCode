class Solution {
    public boolean checkString(String s) {
        boolean found = false;

        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == 'b')
                found = true;
            if(found && s.charAt(i) == 'a')
                return false;
        }

        return true;
    }
}
