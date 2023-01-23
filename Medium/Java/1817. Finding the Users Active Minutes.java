class Solution {
    public int[] findingUsersActiveMinutes(int[][] logs, int k) {
        int[] uam = new int[k];
        
        // Store each user's activity into a map
        Map<Integer, Set<Integer>> activity = new HashMap<>();
        for(int[] i : logs){
            if(!activity.containsKey(i[0]))
                activity.put(i[0], new HashSet<>());
            activity.get(i[0]).add(i[1]);
        }

        // Count the size of each user's activity, and store it
        // in the uam array
        for(int key : activity.keySet()){
            uam[activity.get(key).size() - 1]++;
        }

        // Return the uam array
        return uam;
    }
}
