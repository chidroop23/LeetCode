# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode() #dummy node so we dont have to worry about inserting into dummy list 
        tail = dummy

        while list1 and list2: # if both are them are non empty 
            if list1.val < list2.val:
                tail.next = list1 # if it is less than l2 then insert it into l1 
                list1 = list1.next # updating the l1 pointer
            else: # if they are less aor equal 
                tail.next = list2 # inserting the l2
                list2 = list2.next
            tail = tail.next  # upadting the tail node

        if list1: #if one of them is empty 
            tail.next = list1
        elif list2: #if one of them is empty 
            tail.next = list2

        return dummy.next