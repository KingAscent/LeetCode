var getTargetCopy = function(original, cloned, target) {
    // Base case
    if(original == null)
        return null;
    
    // Current node is cloned
    if(original == target)
        return cloned;
    
    // See if left tree or right tree has a target
    return getTargetCopy(original.left, cloned.left, target) ||
           getTargetCopy(original.right, cloned.right, target);
};
