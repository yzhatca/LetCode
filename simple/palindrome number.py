# def isPalindrome(x):
#     nums_str = str(x)
#     #mid 为开始比较的位置
#     mid = len(nums_str) // 2
#     stack = []
#     for char in nums_str[:mid]:
#         stack.append(char)
#     if len(nums_str) % 2 != 0:
#         mid += 1
#     for char in nums_str[mid:]:
#         if char != stack.pop():
#             return False
#     return True

# using two pointers 
def isPalindrome(x):    
    nums_str = str(x)
    left = 0
    right = len(nums_str) -1
    while left < right and left != right:
        if nums_str[left] != nums_str[right]:
            return False
        left += 1
        right -=1
    return True
    
print(isPalindrome(1221))
        
