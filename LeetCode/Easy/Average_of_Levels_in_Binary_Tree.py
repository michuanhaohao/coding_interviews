'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # 层序遍历
        queue = [root, None] # 每层之间用 None 相隔
        res = []
        temp = 0
        count = 0
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur != None:
                temp += cur.val
                count += 1
                if cur.left != None:
                    queue.append(cur.left)
                if cur.right != None:
                    queue.append(cur.right) 
                if queue[0] == None and len(queue) != 1: # 下一个元素为None，即当前元素是该层的最后一个元素，而且下一层还有元素
                    queue.append(None)
            else: # 到下一层
                res.append(float(temp) / count)
                temp = 0
                count = 0
        return res

