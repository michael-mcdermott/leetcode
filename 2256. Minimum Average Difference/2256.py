class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        
        length = len(nums)
        print(f'length is {length}')
        
        total = 0
        for i in nums:
            total += i
            print(total)
            leftList = [nums[:i]]
            rightList = [nums[i:]]
            print(leftList, rightList)


if __name__== "__main__" :
        
        solution = Solution
        nums = [2,5,3,9,5,3]
        print(solution.minimumAverageDifference(solution, nums))