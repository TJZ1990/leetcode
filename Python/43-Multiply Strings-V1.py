#use a list to store result
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        product = [0] * (len(num1)+len(num2))
        for i1 in reversed(range(len(num1))):
            for i2 in reversed(range(len(num2))):
                product[i1+i2+1] += int(num1[i1])*int(num2[i2]) 
                product[i1+i2] += product[i1+i2+1] / 10
                product[i1+i2+1] %= 10
        
        while len(product) > 1 and product[0] == 0:
            product.pop(0)
        
        return "".join(map(str, product))
