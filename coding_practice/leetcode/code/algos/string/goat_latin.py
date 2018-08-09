# https://leetcode.com/problems/goat-latin/description/
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        gl_words = list()
        vowels = "aeiou"
        for i,w in enumerate(S.split(' ')):
            postfix = 'ma'+'a'*(i+1)
            if w[0].lower() in vowels:
                gl_words.append(w+postfix)
            else:
                gl_words.append(w[1:]+w[0]+postfix)
        return ' '.join(gl_words)
