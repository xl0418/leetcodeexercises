class Solution(object):
    def canCompleteCircuit(self, gas,cost):
        remain = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(remain) < 0:
            return -1
        else:
            remain_gas = 0
            output = 0
            for i in range(len(gas)):
                remain_gas += remain[i]
                if remain_gas < 0:
                    remain_gas = 0
                    output = i + 1

            return output

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
gascost = Solution()
gascost.canCompleteCircuit(gas,cost)
