# 给定一个二叉树，返回它的中序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 
# 输出: [1,3,2] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ## 迭代法
        stack = [root]
        ans = []
        while stack:
            cur = stack.pop()
            if isinstance(cur, TreeNode):
                stack.extend([cur.right, cur.val, cur.left])
            elif isinstance(cur, int):
                ans.append(cur)
        return ans

        ## 递归法
        '''ans=[]
        if root:
            if root.left: self.help(root.left,ans)
            ans.append(root.val)
            if root.right:self.help(root.right,ans)
        return ans
    def help(self,root,ans):
        if root.left: self.help(root.left, ans)
        ans.append(root.val)
        if root.right: self.help(root.right, ans)'''

# leetcode submit region end(Prohibit modification and deletion)
