class Solution {
    public String removeTrailingZeros(String num) {
        int end = num.length();

        for(int i = num.length() - 1; 0 <= i; i--){
            if(num.charAt(i) != '0'){
                end = i + 1;
                break;
            }
        }

        return num.substring(0, end);
    }
}
