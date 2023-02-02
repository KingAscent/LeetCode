class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        for(int i = 0; i < words.length - 1; i++){
            String w1 = words[i];
            String w2 = words[i + 1];
            if(!isAlienSortedHelper(w1, w2, order))
                return false;
        }
        
        return true;
    }

    private boolean isAlienSortedHelper(String w1, String w2, String order){
        if(w1.equals(w2))
            return true;

        int min = Math.min(w1.length(), w2.length());
        int j = 0;
        while(j < min && w1.charAt(j) == w2.charAt(j)){
            j++;
        }
        if(j == min){
            return min == w1.length();
        }else{
            char c1 = w1.charAt(j);
            char c2 = w2.charAt(j);
            return order.indexOf(c1) < order.indexOf(c2);
        }
    }
}
