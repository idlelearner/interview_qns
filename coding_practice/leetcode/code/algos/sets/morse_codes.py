class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = set()
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            m = ''.join([morse_codes[ord(c)-97] for c in word])
            if m not in res:
                res.add(m)
                
        return len(res)

if __name__ == '__main__':
    s = Solution()
    print s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])