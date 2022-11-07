class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        // Map that will be ordered by height later, with names attached to each height
        // String array that will be returned
        HashMap<Integer, String> map = new HashMap();
        String ordered[] = new String[names.length];

        // Put all of the names into the map
        for(int i = 0; i < names.length; i++){
            map.put(heights[i], names[i]);
        }

        // Order all of the names by height
        List<Integer> list = new ArrayList(map.keySet());
        Collections.sort(list, Collections.reverseOrder());

        // For each value in the list, add each name associated with each height
        // into the String array ordered.
        int a = 0;
        for(int i: list){
            ordered[a] = map.get(i);
            a++;
        }

        // Return the string array
        return ordered;
    }
}
