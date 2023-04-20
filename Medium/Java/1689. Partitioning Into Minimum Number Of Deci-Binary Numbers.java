class Solution {
    public int minPartitions(String n) {
        int db = 0;

        for(int i = 0; i < n.length(); i++){
            db = Math.max(db, n.charAt(i) - '0');
        }

        return db;
    }
}
