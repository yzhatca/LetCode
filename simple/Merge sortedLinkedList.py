class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def mergeTwoLists(list1, list2):
#     #创建一个虚拟节点来保存合并后的链表
#     temp = ListNode()
#     # 指向合并链表中当前节点的指针
#     current = temp
#     while list1 and list2:
#         if list1.val <= list2.val:
#             current.next = list1
#             list1 = list1.next
#         else:
#             current.next = list2
#             list2 = list2.next
        
#         current = current.next
    
#     # python中三元表达式
#     # 将剩余的非空链表直接连接到合并链表的末尾
#     current.next = list1 if list1 else list2    
    
#     return temp.next

def mergeTwoLists(self,list1, list2):
    # base condition
    # 如果list1为空，说明list1中已经没有节点剩余，并且完成了排序,则返回另一个链表
    # 另一个链表中的所有节点都可以直接添加到合并后的链表中，因为这个非空链表已经是有序的。
    if not list1:
        return list2  
    if not list2:
        return list1
    
    # 递归地比较两个链表的头节点值，并将较小节点的下一个节点更新为合并后的链表
    if list1.val < list2.val:
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = self.mergeTwoLists(list2.next,list1)
        return list2