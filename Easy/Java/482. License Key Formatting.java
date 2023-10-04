class Solution {
    public String licenseKeyFormatting(String s, int k) {
        StringBuilder license = new StringBuilder();

        for(int i = s.length() - 1; 0 <= i; i--){
            if(s.charAt(i) != '-'){
                if(license.length() % (k + 1) == k)
                    license.append('-');
                license.append(s.charAt(i));
            }
        }

        return license.reverse().toString().toUpperCase();
    }
}
