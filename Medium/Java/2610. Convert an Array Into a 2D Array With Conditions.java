class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        int n = nums.length;
        int[] freq = new int[n + 1];
        int max = 0;
        List<List<Integer>> list = new ArrayList<>();

        for(int num : nums){
            freq[num]++;
            max = Math.max(max, freq[num]);
        }

        for(int i = 0; i < max; i++){
            list.add(new ArrayList<>());
        }
        
        for(int i = 0; i <= n; i++){
            while(0 < freq[i]--){
                list.get(freq[i]).add(i);
            }
        }

        return list;
    }
}
