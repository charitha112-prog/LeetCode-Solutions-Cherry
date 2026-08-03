class Solution(object):
    def maxProfit(self, prices):
        min=float('inf')
        max=0
        for p in prices:
            if p<min:
                min= p
            profit=p-min
            if profit>max:
                max=profit
        return max
        