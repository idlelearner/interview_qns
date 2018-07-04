# check if the string is palindrome
def is_palindrome(s):
    return s == s[::-1]

def longest_palindrome(s):
    longest_palindrome = ""
    for i in range(len(s)):
        l=0
        # odd length palindromes
        while i-l>=0 and i+l<len(s):
            substr = s[i-l:i+1+l]
            if is_palindrome(substr):
                if len(longest_palindrome)<len(substr):
                    longest_palindrome = substr
                l=l+1
            else:
                break
        l=0
        # even length palindromes
        while i-l>=0 and i+1+l<len(s):
            substring = s[i-l:i+2+l]
            if is_palindrome(substring):
                if len(longest_palindrome)<len(substring):
                    longest_palindrome = substring
                l=l+1
            else:
                break

    return longest_palindrome

if __name__ == '__main__':
    print longest_palindrome('ababad')
    print longest_palindrome('cbbd')
    print longest_palindrome('ababa')
    print longest_palindrome('')
    print longest_palindrome('dasat')
