class Solution {
    public int furthestDistanceFromOrigin(String moves) {
        int countL = 0;
        int countR = 0;
        int countBlanks = 0;
        
        for(int i = 0; i < moves.length(); i++){
            if(moves.charAt(i) == 'L')
                countL++;
            else if(moves.charAt(i) == 'R')
                countR++;
            else
                countBlanks++;
        }

        return Math.abs(countL - countR) + countBlanks;
    }
}
