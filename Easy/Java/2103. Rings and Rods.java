class Solution {
    public int countPoints(String rings) {
        int count = 0;
        int[] red = new int[10];
        int[] blue = new int[10];
        int[] green = new int[10];

        // Even positions of rings
        for(int i = 0; i < rings.length(); i += 2){
            char c = rings.charAt(i);
            int index = rings.charAt(i + 1) - '0';
            if(c == 'R')
                red[index]++;
            if(c == 'B')
                blue[index]++;
            if(c == 'G')
                green[index]++;
        }

        // Odd positions of rings
        for(int i = 0; i < 10; i++){
            if(red[i] != 0 && blue[i] != 0 && green[i] != 0)
                count++;
        }

        return count;
    }
}
