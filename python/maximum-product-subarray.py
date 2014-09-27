class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 1:
            return A[0]
        maxP = 0
        nega = False
        p = 0
        q = 0 
        for k in A:
            if k == 0:
                p = 0
                q = 0
                nega = False
            else:
                if p == 0:
                    p = 1
                p *= k
                if nega:
                    if q == 0:
                        q = 1
                    q *= k
                else:
                    if k < 0:
                        nega = True
            maxP = max(maxP,p,q)
        return maxP
#
# for any subarray without 0, 
#
# + .... + - + + - + + + - - - - - + + ....
# _________________________________________---->Product1  : p
#            ______________________________---->Product2  : q
# 
# Product2 does not contain the first negative number and the array before it.
#
# maxP is updated in each step, so it will cover the answer.  
#
# or , you may comprehend the following:
#
# + + + + - + + - + + + - - - + - - + + + 
# _______________________________________---->ProductA
#           _____________________________---->ProductB   (starts after the first negative number)
# _______________________________        ---->ProductC   (ends before the last negative number)
# 
# if ProductA is positive, it's the max product of the subarray
# if ProductA is negative, the max product is either ProductB or ProductC
#