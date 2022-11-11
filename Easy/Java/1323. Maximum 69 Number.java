class Solution {
    public int maximum69Number (int num) {
        char[] numbers = Integer.toString(num).toCharArray();
        for(int i = 0; i < numbers.length; i++){
            if(numbers[i] == '6'){
                numbers[i] = '9';
                i = numbers.length;
            }
        }
        return Integer.parseInt(String.valueOf(numbers));
    }
}
