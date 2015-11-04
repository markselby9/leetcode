# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (headA == None) | (headB == None): return None
        node1 = headA
        node2 = headB
        len1 = 1
        len2 = 1
        while node1.next != None:
            node1 = node1.next
            len1+=1
        while node2.next != None:
            node2 = node2.next
            len2+=1
        diff = len1 - len2
        node1 = headA
        node2 = headB
        if diff>0:
            for i in range(diff):
                node1 = node1.next
        if diff<0:
            for i in range(0-diff):
                node2 = node2.next
        if node1 == node2: return node1
        while node1.next != None:
            if (node1 == node2): return node1
            node1 = node1.next
            node2 = node2.next
        return None
            
sol = Solution()
print sol.getIntersectionNode()