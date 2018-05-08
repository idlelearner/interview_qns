def memodict(f):
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            print 'missing called'
            ret = self[key] = f(key)
            return ret 
    return memodict().__getitem__

@memodict
def f(a):
    return 1+a

print f(1)
print f(1)
print f(4)

#multiple arguments
def memoize(f):
    """ Memoization decorator for a function taking one or more arguments. """
    class memodict(dict):
        def __getitem__(self, *key):
            return dict.__getitem__(self, key)

        def __missing__(self, key):
            ret = self[key] = f(*key)
            return ret

    return memodict().__getitem__