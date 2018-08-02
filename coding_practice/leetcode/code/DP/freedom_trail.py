from collections import defaultdict

# Need to work on this:
# https://leetcode.com/problems/freedom-trail/hints/
def findRotateSteps(ring, key):
        char_pos, n = defaultdict(list), len(ring)
        for i, ch in enumerate(ring):
            char_pos[ch].append(i)
        #@lru_cache(maxsize=None)    
        def dfs(cur, target):
            if target == len(key):
                return 0
            return min(1 + min(abs(cur - option), n - abs(cur - option)) + dfs(option, target + 1) for option in char_pos[key[target]])
        return dfs(0, 0)


if __name__=='__main__':
    print findRotateSteps("godding", "d")