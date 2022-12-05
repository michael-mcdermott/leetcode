class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        preSum = [nums[0]]
        for i in range(1, len(nums)):
            preSum.append(preSum[i-1] + nums[i])

        min_diff = float('inf')
        min_idx = 0

        for i in range(len(preSum)):
            diff = abs(preSum[i]//(i+1) - (preSum[-1] - preSum[i])//max(len(preSum)-1 -i,1 ) )

            if diff < min_diff:
                min_diff = diff
                min_idx = i

        return min_idx


if __name__== "__main__" :
        
    solution = Solution
    nums = [2,5,3,9,5,3]
    print(solution.minimumAverageDifference(solution, nums))