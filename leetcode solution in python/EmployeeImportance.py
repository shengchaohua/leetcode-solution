# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 10:29:19 2019

@problem: leetcode 690. Employee Importance

@author: shengchaohua
"""

# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # Recursive solution
#        e_imp, e_subs = [[e.importance, e.subordinates] \
#                         for e in employees if e.id == id][0]
#        return sum([self.getImportance(employees, s) for s in e_subs]) + e_imp
        
        # Interative solution
#        e_queue = [id]
#        totals = []
#        while e_queue:
#            e_id = e_queue.pop(0)
#            totals.append(e_id)
#            e_subs = [e.subordinates for e in employees if e.id == e_id][0]
#            e_queue.extend(e_subs)
#        return sum([e.importance for e in employees if e.id in totals])
    
        # Reference approach.
        emap = {e.id: e for e in employees}
        def dfs(eid):
            employee = emap[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates))
        return dfs(id)
        

def test():
    s = Solution()
    employees = [Employee(1,5,[2,3]), Employee(2,3,[]), Employee(3,3,[])]
    p_id = 1
    print(s.getImportance(employees, p_id))
    
    
if __name__ == '__main__':
    test()
    