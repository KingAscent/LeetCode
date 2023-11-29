class Solution {
    public String convertToBase7(int num) {
        if(num == 0)
            return "0";

        String neg = 0 <= num ? "" : "-";
        String base7 = "";
        num = Math.abs(num);

        while(1 <= num){
            base7 = Integer.toString(num % 7) + base7;
            num = num / 7;
        }

        return neg + base7;
    }
}
