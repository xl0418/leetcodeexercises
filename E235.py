# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mathernode(self,root,node):
        if node == root[0]:
            return root[0]
        else:
            node_index = root.index(node) +1
            done = True
            i = 0
            while not ((node_index > 2 ** i - 1) and (node_index <= 2 ** (i + 1) - 1)):
                i += 1
            motherindex = round((node_index-2**i+1)/2)  -1
            mothernodeval = root[2**(i-1)-1+motherindex]

            return mothernodeval

    def lowestCommonAncestor(self, root, p, q):
        pmother_list = [p]
        while p != root[0]:
            p = self.mathernode(root,p)
            pmother_list.append(p)

        while q not in pmother_list:
            q = self.mathernode(root,q)

        return q


root = [6,2,8,0,4,7,9,None,None,3,5]
p = 7
q = 5

test = Solution()
test.lowestCommonAncestor(root,p,q)
