
def printHash(nums):
    nums_item = {}
    
    #enumerate方法用于将可迭代对象（如列表、元组、字符串等）转换为一个枚举对象，它生成一组由索引和值组成的元组。
    #每个元组中的第一个元素是索引，第二个元素是对应位置的值。
    for index,value in enumerate(nums):
        nums_item[index] = value
    print(nums_item)
    
nums = [1,2,3,4,5,6]
printHash(nums)
