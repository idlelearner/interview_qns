def check_matching_paranthesis(paranthesis):
    stck = []
    for v in paranthesis:
        if v == "(":
            stck.append(v)
        else:
            stck.pop()

    return False if stck else True

print check_matching_paranthesis('(())(')