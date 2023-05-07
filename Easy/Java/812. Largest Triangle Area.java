class Solution {
    public double largestTriangleArea(int[][] points) {
        int n = points.length;
        double largest = 0;

        for(int i = 0; i < n; i++){
            for(int j = i + 1; j < n; j++){
                for(int k = j + 1; k < n; k++){
                    double temp = 0;
                    int[] a = points[i];
                    int[] b = points[j];
                    int[] c = points[k];
                    temp = Math.abs(area(a, b) + area(b, c) + area(c, a));
                    largest = Math.max(largest, temp);
                }
            }
        }

        return largest;
    }

    public double area(int[] a, int[] b){
        double base = b[0] - a[0];
        double height = a[1] + b[1];
        return 0.5 * base * height;
    }
}
