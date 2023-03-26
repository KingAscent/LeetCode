public class Solution extends GuessGame {
    public int guessNumber(int n) {
        if(n == 1)
            return 1;
        if(guess(n) == 0)
            return n;
        
        int first = 1;
        int last = n;
        int pick = 0;

        while(first < last){
            pick = first + (last - first) / 2;
            int temp = guess(pick);
            if(temp == 0){
                break;
            }else if(temp == -1){
                last = pick;
            }else{
                first = pick;
            }
        }
      
        return pick;
    }
}
