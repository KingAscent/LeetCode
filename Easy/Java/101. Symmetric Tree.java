class Solution {
    public boolean isSymmetric(TreeNode root) {
        return checkSymmetry(root, root);
    }

    public boolean checkSymmetry(TreeNode leftTree, TreeNode rightTree){
        if(leftTree == null && rightTree == null)
            return true;
        
        if(leftTree != null && rightTree != null && leftTree.val == rightTree.val){
            Boolean outer = checkSymmetry(leftTree.left, rightTree.right);
            Boolean inner = checkSymmetry(leftTree.right, rightTree.left);
            return outer && inner;
        }

        return false;
    }
}
