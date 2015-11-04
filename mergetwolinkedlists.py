# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer = ListNode(-1)
        return_answer = answer
        if l1==None:
            return l2
        if l2==None:
            return l1
        while (l1.next != None) & (l2.next != None):
            if l1.val < l2.val:
                answer.next = l1
                l1 = l1.next
                answer = l1
            else:
                answer.next = l2
                l2 = l2.next
                answer = l2

        while l1.next != None:
            answer.next = l1
            l1 = l1.next
            answer = l1
        while l2.next != None:
            answer.next = l2
            l2 = l2.next
            answer = l2
        return return_answer.next