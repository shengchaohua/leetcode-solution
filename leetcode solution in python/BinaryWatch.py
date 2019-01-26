# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 12:56:58 2019

@problem: leetcode 401. Binary Watch

@author: shengchaohua
"""

class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hours = [['0'],
                 ['1', '2', '4', '8'],
                 ['3', '5', '9', '6', '10'],
                 ['7', '11']
                ]
        minutes = [['00'],
                   ['01', '02', '04', '08', '16', '32'], 
                   ['03', '05', '09', '17', '33', '06', '10', '18', '34', '12', '20', '36', '24', '40', '48'], 
                   ['07', '11', '19', '35', '13', '21', '37', '25', '41', '49', '14', '22', '38', '26', '42', '50', '28', '44', '52', '56'], 
                   ['15', '23', '39', '27', '43', '51', '29', '45', '53', '57', '30', '46', '54', '58'], 
                   ['31', '47', '55', '59']
                  ]
        res = []
        for n in range(num, -1, -1):
            if n >= 4 or num - n >= 6: 
                continue
            for h in hours[n]:
                for m in minutes[num - n]:
                    res.append(h + ':' + m)

        return res
    
        # Solution from @StefanPochmann
#        return ['%d:%02d' % (h, m) 
#                for h in range(12) for m in range(60) 
#                if (bin(h) + bin(m)).count('1') == num]
    

def test():
    s = Solution()
    print(s.readBinaryWatch(5))
    

if __name__ == '__main__':
    test()