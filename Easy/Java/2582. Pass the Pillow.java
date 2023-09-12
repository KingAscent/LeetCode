class Solution {
    public int passThePillow(int n, int time) {
        int place = 0;
        int direction = time / (n - 1);
        int remainder = time % (n - 1);

        if(direction % 2 == 0)
            place = remainder + 1;
        else
            place = n - remainder;
        
        return place;
    }
}
