'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6]
'''

def prod_except_current_division(lst):
    product = 1
    for elmt in lst:
        product *= elmt
    return [product/v for v in lst]


def prod_except_current_no_division(lst):
    if len(lst)==1:
        return [1]
    prefix_prod = []
    postfix_prod = []
    product = 1
    for v in lst:
        product *= v
        prefix_prod.append(product)
    product = 1
    for v in range(len(lst), 0, -1):
        product *= v
        postfix_prod.append(product)
    postfix_prod = postfix_prod[::-1]
    res = []
    res.append(postfix_prod[1])
    for i in range(1,len(lst)-1):
        res.append(prefix_prod[i-1]*postfix_prod[i+1])
    res.append(prefix_prod[len(lst)-2])
    return res


if __name__ == '__main__':
    print prod_except_current_division([1, 2, 3, 4, 5])
    print prod_except_current_no_division([1, 2, 3, 4, 5])
    print prod_except_current_division([1])
    print prod_except_current_no_division([1])
    print prod_except_current_division([1,2])
    print prod_except_current_no_division([1,2])