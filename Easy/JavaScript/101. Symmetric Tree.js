var isSymmetric = function(root) {
    return checkSymmetry(root, root);
};

var checkSymmetry = function(leftTree, rightTree) {
    if(leftTree == null && rightTree == null)
        return true;
    
    if(leftTree != null && rightTree != null && leftTree.val == rightTree.val){
        let outer = checkSymmetry(leftTree.left, rightTree.right);
        let inner = checkSymmetry(leftTree.right, rightTree.left);
        return outer && inner;
    }

    return false;
}
