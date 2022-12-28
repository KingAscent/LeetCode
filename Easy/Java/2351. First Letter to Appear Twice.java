class Solution {
    public char repeatedCharacter(String s) {
        Map<Character, Integer> count = new HashMap<>();
        char twice = 'a';

        for(int i = 0; i < s.length(); i++){
            if(!count.containsKey(s.charAt(i)))
                count.put(s.charAt(i), 1);
            else{
                twice = s.charAt(i);
                break;
            }
        }

        return twice;
    }
}
