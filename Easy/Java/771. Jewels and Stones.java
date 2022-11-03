class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        // Create a set to contain the different types of jewels
        // Count of jewels amongst the stones
        Set<Character> set = new HashSet<Character> ();
        int count = 0;
        
        // Add the different jewels into the set
        for(int i = 0; i < jewels.length(); i++){
            set.add(jewels.charAt(i));
        }

        // Go over the stones, looking for jewels
        for(int i = 0; i < stones.length(); i++){
            if(set.contains(stones.charAt(i)))
                count++;
        }
        
        // Return the count of jewels
        return count;
    }
}
