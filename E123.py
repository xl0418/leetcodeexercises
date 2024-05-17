class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        pro_interval = []
        p_start = prices[0]
        p_end = prices[0]
        for i in range(len(prices) - 1):
            if prices[i + 1] >= prices[i]:
                p_end = prices[i + 1]
                if i == len(prices) -2:
                    pro_interval.append([p_start, p_end])
            else:
                if p_start < p_end:
                    pro_interval.append([p_start, p_end])
                p_start = prices[i + 1]
                p_end = prices[i + 1]

        if len(pro_interval) == 0:
            return 0
        else:
            len_prointerval = len(pro_interval)
            while len_prointerval > 2:
                rm_id = []
                for i in range(len_prointerval - 1):
                    current_int = pro_interval[i]
                    next_int = pro_interval[i + 1]
                    profit_int1 = current_int[1] - current_int[0]
                    profit_int2 = next_int[1] - next_int[0]
                    if current_int[0] > next_int[0] and current_int[1] > next_int[1]:
                        if profit_int1 < profit_int2:
                            rm_id.append(i)
                        else:
                            continue
                    elif current_int[0] > next_int[0] and current_int[1] < next_int[1]:
                        rm_id.append(i)
                    elif current_int[0] < next_int[0] and current_int[1] > next_int[1]:
                        continue
                    else:
                        if i < len_prointerval - 2:
                            if profit_int1 < profit_int2:
                                rm_id.append(i)
                                next_int[0] = current_int[0]
                            else:
                                continue
                        else:
                            break

                if len_prointerval - len(rm_id) < 2:
                    del rm_id[1]

                for id in sorted(rm_id, reverse=True):
                    del pro_interval[id]
                len_prointerval = len(pro_interval)
            max_profit = 0
            for final_int in pro_interval:
                max_profit += final_int[1] - final_int[0]
            return max_profit




if __name__ == "__main__":
    prices = [1,2,4,2,5,7,2,4,9,0,9]
    solution = Solution()
    maxp = solution.maxProfit(prices)