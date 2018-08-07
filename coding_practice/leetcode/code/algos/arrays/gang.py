# Complete the isOneGang function below.
def isOneGang(criminalsAndCrimes):
    no_of_criminals = len(criminalsAndCrimes)
    if no_of_criminals == 1: return "TRUE"
    # convert the array string to set of integers
    crime_set = [set(map(int, criminalsAndCrimes[i])) for i in range(no_of_criminals)]
    # Gang contains the set of criminals
    gang = set()
    for i in xrange(0, no_of_criminals-1, 1):
        for j in xrange(i+1, no_of_criminals, 1):
            # if i or j criminal is not processed
            if i not in gang or j not in gang:
                # check if they have committed common crimes
                if crime_set[i].intersection(crime_set[j]):
                    gang.add(i)
                    gang.add(j)
                # if gang has all the criminals, return True
                if len(gang)==no_of_criminals:
                    return "TRUE"
    return "FALSE"


def isOneGang(criminalsAndCrimes):
    no_of_criminals = len(criminalsAndCrimes)
    if no_of_criminals == 1: return "TRUE"
    # Gang contains the set of criminals
    gang = set()
    crime_dict = dict()
    for i in xrange(0, no_of_criminals, 1):
        for j in xrange(0, len(criminalsAndCrimes[i]), 1):
            # if i or j criminal is not processed
                if crime_dict.get(criminalsAndCrimes[i][j]):
                    gang.add(i)
                    gang.add(j)
                else:
                    crime_dict[criminalsAndCrimes[i][j]] = True
                    # if gang has all the criminals, return True
                if len(gang)==no_of_criminals:
                    return "TRUE"
    return "FALSE"


if __name__=='__main__':
    print isOneGang([["1","2"],["3","1"],["5","4"]])
