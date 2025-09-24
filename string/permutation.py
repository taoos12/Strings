# Most asked question 
# Question asked in interviews of companies like [Google,microsoft,apple,meta,amazon,oracle,adobe,paypal,VM Ware]
# level of difficulty = Medium

# Write a function that returns all possible permutations of a given string.
# Avoid using python's iteratools.permutations() and instead implement your own logic

# Example
# input = 'abc'
# output = ['abc','acb','bac','bca','cab','cba']

# Base case -> Loop single character -> substring -> recursion -> join -> result return


def find_permutations(s):
    # Base case
    if len(s)==1:
        return [s]
    
    permutations = []

    for i in range(len(s)):
        current_char = s[i]
        remaining_char = s[:i] + s[i+1:]

        remaining_permutations = find_permutations(remaining_char)

        for p in remaining_permutations:
            permutations.append(current_char + p)

    return permutations


print(find_permutations('abc'))