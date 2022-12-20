// Can be made cleaner using a set or an array, but this solution has a lower
// runtime and memory usage
class Solution {
    public boolean halvesAreAlike(String s) {
        int front = 0;
        int back = 0;
        String frontHalf = s.toLowerCase().substring(0, s.length() / 2);
        String backHalf = s.toLowerCase().substring(s.length() / 2);

        for(int i = 0; i < frontHalf.length(); i++){
            if(frontHalf.charAt(i) == 'a' || 
               frontHalf.charAt(i) == 'e' ||
               frontHalf.charAt(i) == 'i' ||
               frontHalf.charAt(i) == 'o' ||
               frontHalf.charAt(i) == 'u')
                front++;
            if(backHalf.charAt(i) == 'a' ||
               backHalf.charAt(i) == 'e' ||
               backHalf.charAt(i) == 'i' ||
               backHalf.charAt(i) == 'o' ||
               backHalf.charAt(i) == 'u')
                back++;
        }
        
        return front == back;
    }
}
