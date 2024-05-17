# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def to_binary_tree(items: list[int]) -> TreeNode:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()



class Solution:
    def rightSideView(self, root) -> list[int]:
        if not root:
            return None
        queue = [root]
        right_most = []
        while len(queue) > 0:
            n = len(queue)
            right_most.append(queue[-1].val)

            for i in range(n):
                element = queue.pop(0)
                if element.left:
                    queue.append(element.left)

                if element.right:
                    queue.append(element.right)

        return right_most

root = to_binary_tree([1,2,3,"null",5,"null",4])
solution = Solution()
solution.rightSideView(root)
