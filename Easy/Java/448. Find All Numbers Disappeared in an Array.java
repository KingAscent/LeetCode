class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> missing = new ArrayList<>();
        int[] count = new int[nums.length];

        for(int i = 0; i < nums.length; i++)
            count[nums[i] - 1]++;
        for(int i = 0; i < nums.length; i++){
            if(count[i] == 0)
                missing.add(i + 1);
        }

        return missing;
    }
}
