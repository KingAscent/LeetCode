class Solution {
    public int[] decompressRLElist(int[] nums) {
        // Find out what the size of the decompressed list is
        int decompressedSize = 0;
        for(int i = 0; i < nums.length; i += 2){
            decompressedSize += nums[i];
        }

        // Initialize an integer array that is the size of the
        // decompressed list
        // Initialize an index value for the decompressedList
        int[] decompressedList = new int[decompressedSize];
        int index = 0;

        // Add all the values into the decompressed list a
        // frequency number of times
        for(int i = 0; i < nums.length; i += 2){
            int freq = nums[i];
            int value = nums[i + 1];
            for(int j = 0; j < freq; j++){
                decompressedList[index] = value;
                index++;
            }
        }

        // Return the decompressedList
        return decompressedList;
    }
}
