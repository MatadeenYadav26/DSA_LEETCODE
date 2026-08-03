class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int

        """

        absolute_value = abs(x)
        result = 0
        
        #reversing:
        while (absolute_value>0):
            remainder = absolute_value % 10 
            result = result*10+remainder
            absolute_value = absolute_value//10

        #negative condition
        if(x<0):
            result = -result

        #Range Handling Out of bonunds
        if(result>=-2**31 and result<2**31-1):
            return result

        return 0