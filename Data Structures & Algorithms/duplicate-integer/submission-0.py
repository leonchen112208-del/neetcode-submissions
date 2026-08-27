class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # Number sort
        left = 0 # sets a left pointer to 0
        right = len(nums) - 1 # sets a right pointer to length of list - 1
        while (left < right): ## while loop takes the () and needs a :
            if nums[left] == nums[left + 1]: ## if the index at the left pointer is EQUAL to the one after it, it will return the True boolean

                return True
            left += 1 ## This just moves the loop through each index
        return False ## returns FAlse if the if statement doesn't run