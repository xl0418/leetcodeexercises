# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

def list_to_LL(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LL(arr[1:]))
class Solution:
    def partition(self, head, x: int):
        if head == None:
            return list_to_LL([])
        else:
            head_vec = []
            do = True
            while do:
                head_vec.append(head.val)

                if head.next == None:
                    do = False
                else:
                    head = head.next

            do_vec = [True]
            while any(do_vec):
                do_vec = [False]
                for i in range(len(head_vec)-1, 0, -1):
                    if head_vec[i] < x and head_vec[i - 1]>=x:
                        temp = head_vec[i]
                        head_vec[i] = head_vec[i-1]
                        head_vec[i-1] = temp
                        do_vec.append(True)
            return list_to_LL(head_vec)





head = list_to_LL([])
x = 3
solution = Solution()
solution.partition(head, x)
