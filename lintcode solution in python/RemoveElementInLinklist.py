# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:57:12 2018

@problem: lintcode No.452 删除链表中等于给定值val的所有节点

@author: sheng
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        while head is not None and head.val == val:
            head = head.next
            
        if head.next is None:
            return head
        
        p = head
        q = head.next
        
        while q is not None:
            if q.val == val:
                 p.next = q.next
                 q = p.next
            else:
                p = q
                q = q.next
                
        return head

def main():
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(1)
    node4 = ListNode(2)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None
    res = s.removeElements(node1, 1)
    while res is not None:
        print(res.val, end=' ')
        res = res.next
    
if __name__ == '__main__':
    main()