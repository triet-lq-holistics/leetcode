# Definition for a binary tree node.
"""https://leetcode.com/problems/minimum-depth-of-binary-tree/description/"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(self, root: TreeNode | None) -> int:
        """
        if root does have child on either left or right node,
        then increase level by 1

        [3], [9,20], 

        1
        /\
      0.5  2
          / \
        null 3
             \
              4
               \ 
                5
        """
        def helper(root):
            if not root:
                return 0
            
            if not root.left and not root.right:
                return 1
            
            elif not root.left:
                return helper(root.right) + 1
            elif not root.right:
                return helper(root.left) + 1
            else:
                left = helper(root.left) + 1
                right = helper(root.right) + 1

                return min(left, right)
        
        return helper(root)


def minDepth(self, root: TreeNode | None) -> int:
    """
    if root does have child on either left or right node,
    then increase level by 1

    [3], [9,20], 

    1
    /\
    null 2
        / \
    null 3
            \
            4
            \ 
            5
    """


    queue = [root]
    level = 0

    while True:
        if not all(queue):
            break

        for node in queue:
            queue = queue[1:]
            
            queue.append(node.left)
            queue.append(node.right)
        
        level += 1     
    
    return level


            
