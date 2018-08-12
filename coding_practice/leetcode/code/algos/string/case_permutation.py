class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        def casePerm(S, i):
            if i>len(S)-1:
                res.append(S)
            else:
                if S[i].isalpha():
                    if S[i].islower():
                        casePerm(S[:i]+ S[i].upper() + S[i+1:], i+1)
                    else:
                        casePerm(S[:i]+ S[i].lower() + S[i+1:], i+1)
                casePerm(S, i+1)
        casePerm(S, 0)
        return res

if __name__=='__main__':
    s = Solution()
    print s.letterCasePermutation("c")