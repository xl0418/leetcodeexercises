# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_LL(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LL(arr[1:]))





head = list_to_LL([4,2,1,3])

solution = Solution()
solution.sortList(head)


def list_to_LL(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LL(arr[1:]))


class Solution:
    def sortList(self, head):
        if head == None:
            return head
        else:
            head_vec = []
            do = True
            while do:
                head_vec.append(head.val)

                if head.next == None:
                    do = False
                else:
                    head = head.next

            return list_to_LL(sorted(head_vec))