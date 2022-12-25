import random
class Solution:
    def captureForts(self, forts: list[int]) -> int:

        captured = []
        cap = 0
        move_id = 0
        while move_id < len(forts) - 1:
            start_v = forts[move_id]

            if start_v == 0:
                move_id += 1
            else:
                sum_next = forts[move_id]
                while sum_next != 0 and move_id < len(forts) - 1:
                    sum_next += forts[move_id + 1]
                    if sum_next == -2 or sum_next == 2:
                        move_id += 1
                        cap = 0
                        break
                    elif sum_next == 0:
                        move_id += 1
                        captured.append(cap)
                        cap = 0
                        break
                    else:
                        move_id += 1
                        cap += 1
        if len(captured) == 0:
            return 0
        else:
            return max(captured)

if __name__ == "__main__":
    forts = [random.randint(-1,1) for i in range(10)]
    sol = Solution()
    capt = sol.captureForts(forts=forts)






