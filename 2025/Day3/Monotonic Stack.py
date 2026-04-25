# Monotonic Stack approach to find the maximum 12-digit number that can be formed by deleting some digits from the input line while maintaining the order of the remaining digits.

def next_greater_element(nums):
    # Initialize the result array with -1
    res = [-1] * len(nums)
    stack = []  # This will store indices

    for i in range(len(nums)):
        # While stack is not empty and current element is 
        # greater than the element at the index on top of stack
        while stack and nums[i] > nums[stack[-1]]:
            # We found the next greater element for the index at the top
            index = stack.pop()
            res[index] = nums[i]
        
        # Push current index onto the stack
        stack.append(i)
        
    return res

# Example Usage:
arr = [2, 1, 2, 4, 3]
print(f"Input:  {arr}")
print(f"Output: {next_greater_element(arr)}")
# Expected Output: [4, 2, 4, -1, -1]