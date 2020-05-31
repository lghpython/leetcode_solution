# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.change(root.right,root.left)

    def change(self,r:TreeNode,l:TreeNode) -> bool:
        # 1. 左右子树比较相等继续操作,
        # if l and r :
        #     if l.val != r.val: return False
        #     else:
        #         # 2. 右子树左右翻转
        #         if r.left or r.right:
        #             r.left,r.right = r.right, r.left
        #         else:
        #             return True
        #         return self.change(r.left,l.left) and self.change(r.right,l.right)
        # elif not r and not l: return True
        # else:  return False
        if not r and not l: return True
        if not l or not r or l.val != r.val: return False
        return self.change(r.right,l.left) and self.change(r.left,l.right)



if __name__ == '__main__':
    pre = TreeNode(0)

    root = TreeNode(1)
    pre.right = root
    root.left = TreeNode(2)
    root.right= TreeNode(2)
    l = root.left

    l.right = TreeNode(4)
    r = TreeNode(2)
    r.left = TreeNode(4) 

    s = Solution()
    print(s.isSymmetric(pre.right))