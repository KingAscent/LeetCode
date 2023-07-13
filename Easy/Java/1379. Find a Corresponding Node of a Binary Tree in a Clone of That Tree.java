class Solution {
    public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
        // Base case
        if(original == null)
            return null;
        
        // Current node is cloned
        if(original == target)
            return cloned;

        // See if left tree or right tree has a target
        TreeNode left = getTargetCopy(original.left, cloned.left, target);
        if(left != null)
            return left;
        else
            return getTargetCopy(original.right, cloned.right, target);
    }
}
