# Write a function that compresses a given string by replacing a sequences of same character by the character followed by the count.
# If the compressed string is not smaller than the original string,return the original string


# input = 'aaabbcc'
# output = 'a3b2c2'

# Traverse string -> sounting character -> append compressed string -> final result

def compressed_str(s):
    compressed_result = []

    count = 1

    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count+=1
        else:
            compressed_result.append(s[i-1]+str(count))
            count = 1

    compressed_result.append(s[-1]+str(count))

    compressed_string = ''.join(compressed_result)

    if len(compressed_string)<len(s):
        return compressed_string
    
    else:
        return s


print(compressed_str('aabbcc'))


