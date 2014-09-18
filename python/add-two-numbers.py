# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode(0)
        p1 = l1
        p2 = l2
        p3 = l3
        c = 0  #进位
        while p1 != None or p2 != None or c > 0:
            a = p1.val if p1 != None else 0
            b = p2.val if p2 != None else 0
            p3.next = ListNode((a+b+c) % 10)
            c = (a+b+c) / 10
            if p1 != None:
                p1 = p1.next
            if p2 != None:
                p2 = p2.next
            p3 = p3.next
        return l3.next