class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        elif m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        else:
            len_nums2 = len(nums2)
            while n > 0:
                if m == 0:
                    max_nums2 = max(nums2)
                    nums1[m + n - 1] = max_nums2
                    del nums2[-1]
                    n += -1
                else:
                    max_nums1 = max(nums1[0:m])
                    max_nums2 = max(nums2)
                    if max_nums2 >= max_nums1:
                        nums1[m + n - 1] = max_nums2
                        del nums2[-1]
                        n += -1
                    else:
                        nums1[m + n - 1] = max_nums1
                        nums1[m - 1] = 0
                        m += -1
            return



if __name__ == '__main__':
    nums1 = [2,0]
    m = 1
    nums2 = [1]
    n = 1
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print(nums1)