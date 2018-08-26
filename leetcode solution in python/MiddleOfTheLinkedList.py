# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 22:54:42 2018

@problem: leetcode No.876 Middle of the Linked List

@author: shengchaohua
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # I think the description of the problem is confusing.
        # In the exmaple 1, the right answer is to return th third node, 
        # i.e. the ListNode(3)
        # In the example 2, the right is to return the second middle node.
        # However, the Testcase here seems to return the first 
        # so that we must notice that during coding.
        slowNode = fastNode = head
        while fastNode and fastNode.next:
            slowNode = slowNode.next
            fastNode = fastNode.next.next
        return slowNode

    
def printLinkedList(node):
    while node is not None:
        print(node.val, end=' ')
        node = node.next
    print()

    
def main():
    s = Solution()
    head = ListNode(-1)
    cur = head
    for i in range(1, 5):
        cur.next = ListNode(i)
        cur = cur.next
    
    printLinkedList(head.next)
    res = s.middleNode(head)
    printLinkedList(res)
    
if __name__ == '__main__':
    main()