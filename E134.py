class Solution(object):
    def canCompleteCircuit(self, gas,cost):
        remain = [gas[i] - cost[i] for i in range(len(gas))]

        if sum(remain)>=0:
            for i in range(len(gas)):
                gas_reorder = gas[i:]+gas[:i]
                cost_reorder = cost[i:]+cost[:i]
                leftgas = 0
                for j in range(len(gas)):
                    leftgas = leftgas + gas_reorder[j]-cost_reorder[j]
                    if leftgas <0:
                        goon = False
                        break
                    else:
                        goon = True
                if goon:
                    return i
            if not goon:
                return -1
        else:
            return -1



gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
gascost = Solution()
gascost.canCompleteCircuit(gas,cost)
