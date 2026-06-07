def is_palindrome(s):
    if s == "":
        return True
    char1 = s[0]
    charend = s[-1]
    if char1 == charend:
        s = s[1:]
        s = s[:-1]
        return is_palindrome(s)
    else:
        return False
def generate_permutations(s):
    permutationlist = []
    stringcharacters = []
    if len(s) < 1:
        return ['']
    if len(s) == 1:
        permutationlist.append(s)
        return permutationlist
    stringcopy = s
    while stringcopy != '':
        stringcharacters.append(stringcopy[0])
        stringcopy = stringcopy[1:]
    for i in range(len(stringcharacters)):
        newstring = s[:i] + s[i+1:]
        for remainingrecursioncalls in generate_permutations(newstring):
            permutationlist.append(stringcharacters[i] + remainingrecursioncalls)
    return permutationlist
def num_paths(m, n):
    if m == 0 or n == 0:
        return 1
    return num_paths(m-1, n) + num_paths(m, n-1)

        

    
    

    
    

