class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1)+len(s2)!=len(s3):    #如果s1+s2和s3不等长
            return False
        mem = [[0 for a in range(len(s2))] for b in range(len(s1))]    #记忆数组
        def match(i,p1,p2):
            if i<0:    #对s3所有元素都匹配完毕，说明找到一解
                return True
            if p1>=0 and p2>=0:    #如果参数合法，从记忆数组中取解，若元素为0，漏到下一步
                if mem[p1][p2]==1:
                    return True
                elif mem[p1][p2]==-1:
                    return False
            b1 = False if p1<0 or s3[i]!=s1[p1] else match(i-1,p1-1,p2)    #对取s1的一个字符和取s2的一个字符，2种情况分别递归求解，递归之前先剪枝
            if b1:
                if p1>0 and p2>0:    #返回值之前先在记忆数组存一下，下次不用重复算了
                    mem[p1][p2]=1
                return True
            b2 = False if p2<0 or s3[i]!=s2[p2] else match(i-1,p1,p2-1)
            if p1>0 and p2>0:        #返回值之前先在记忆数组存一下，下次不用重复算了
                mem[p1][p2]=1 if b2 else -1 
            return b2
        return match(len(s3)-1,len(s1)-1,len(s2)-1)