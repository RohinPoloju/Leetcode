# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        i = 0
        if not head:
            return head
        if not head.next:
            return head
        length = 0
        length_node = head
        while length_node:
            length += 1
        k = k % length
        print(k)
        while i < k:
            tail = head.next
            beforeTail = head
            while tail.next:
                beforeTail = tail
                tail = tail.next
            tail.next = head
            head = tail
            beforeTail.next = None
            i += 1
        return head

