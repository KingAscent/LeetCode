var sumOfLeftLeaves = function(root) {
    if(root == null || (root.left == null && root.right == null))
        return 0;
    
    let sum = 0;
    if(root.left != null && root.left.left == null && root.left.right == null)
        sum += root.left.val;
    
    return sum + sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right);
};
