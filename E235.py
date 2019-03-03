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
            while done:
                node_index = node_index - 2**i
                if node_index <=0:
                    done = False
                    motherindex = (node_index+2**i+1) // 2
                else:
                    i += 1
            mothernodeval = root[int(2**(i-2)) + motherindex-1]
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
p = 0
q = 9

test = Solution()
test.lowestCommonAncestor(root,p,q)
