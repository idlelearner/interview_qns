# check if the string is palindrome
def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    print is_palindrome('kayak')
    print is_palindrome('hello')
    print is_palindrome('')
