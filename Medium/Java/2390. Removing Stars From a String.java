class Solution {
    public String removeStars(String s) {
        Stack<Character> starless = new Stack();

        for(char c : s.toCharArray()){
            if(c != '*')
                starless.push(c);
            else
                starless.pop();
        }

        StringBuilder new_s = new StringBuilder();
        for(char c : starless){
            new_s.append(c);
        }

        return new_s.toString();
    }
}
