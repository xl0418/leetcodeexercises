from collections import defaultdict

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root




class Solution:
    def zigzagLevelOrder(self, root):
        level_list = defaultdict(list)
        que = []
        que.append([root, 0])
        while len(que) > 0:
            tip_val, tip_level = que.pop(0)
            if tip_val != None:
                level_list[tip_level].append(tip_val.val)
                que.append([tip_val.left, tip_level + 1])
                que.append([tip_val.right, tip_level + 1])

        ans = []
        for lvl in level_list:
            if lvl % 2 ==0:
                ans.append(level_list[lvl])
            else:
                ans.append(level_list[lvl][::-1])


        return ans




root = deserialize('[3,9,20,null,null,15,7]')
solution = Solution()
solution.zigzagLevelOrder(root)