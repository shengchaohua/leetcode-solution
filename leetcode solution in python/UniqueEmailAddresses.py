# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 15:54:56 2018

@problem: leetcode 929. Unique Email Addresses

@author: shengchaohua
"""

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        for em in emails:
            em_spl = em.split('@')
            local_name = em_spl[0]
            domain_name = em_spl[1]
            plus_idx = local_name.find('+')
            if  -1 != plus_idx:
                local_name = local_name[0:plus_idx]
            local_name = ''.join(local_name.split('.'))
            res.add('@'.join([local_name, domain_name]))
        
        return len(res)
    
    
def test():
    s = Solution()
    emails = ["test.email+alex@leetcode.com",
              "test.e.mail+bob.cathy@leetcode.com",
              "testemail+david@lee.tcode.com"]
    print(s.numUniqueEmails(emails))
    
    
if __name__ == '__main__':
    test()
            