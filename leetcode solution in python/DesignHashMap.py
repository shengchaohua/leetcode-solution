# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 12:06:38 2019

@problem: leetcode 706. Design HashMap

@author: shengchaohua
"""

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = [-1] * 1000000

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        self.m[key] = value 

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.m[key]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        self.m[key] = -1


def test():
    # Your MyHashMap object will be instantiated and called as such:
    # obj = MyHashMap()
    # obj.put(key,value)
    # param_2 = obj.get(key)
    # obj.remove(key)
    hashMap = MyHashMap();
    hashMap.put(1, 1);          
    hashMap.put(2, 2);         
    print(hashMap.get(1));      # returns 1
    print(hashMap.get(3));      # returns -1 (not found)
    hashMap.put(2, 1);          # update the existing value
    print(hashMap.get(2));      # returns 1 
    hashMap.remove(2);          # remove the mapping for 2
    print(hashMap.get(2));      # returns -1 (not found)
    

if __name__ == '__main__':
    test()