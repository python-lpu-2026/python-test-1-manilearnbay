"""
Find Second Highest Number

Write a function:
def second_highest(nums):

Requirements:
- Return the second highest unique number
- List may contain duplicates
- If second highest doesn’t exist → return None
- Handle invalid inputs safely

Examples:
second_highest([10, 20, 30]) -> 20
second_highest([5, 5, 5]) -> None
second_highest([-1, -2, -3]) -> -2
"""

def second_highest(nums):
    try:
        unique = list(set(nums))
        
        if len(unique) < 2:
            return None
        unique.sort(reverse=True)
        return unique[1]
    except Exception:
        return None
