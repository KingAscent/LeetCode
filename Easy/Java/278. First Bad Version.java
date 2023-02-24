public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int first = 0;
        int last = n;
        int ver = 0;

        while(first <= last){
            int temp = first + (last - first) / 2;
            if(isBadVersion(temp)){
                ver = temp;
                last = temp - 1;
            }
            else{
                first = temp + 1;
            }
        }

        return ver;
    }
}
