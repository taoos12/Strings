# Write a function to find the index of first non-repeating character in a string
# Input:"swiss"
# Output:"w"(The character"s" repeats, but "w" is the first non-repeating character)

def first_non_repeating_char(s):
    char_count={}

    for char in s:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    
    for i in range(len(char_count)):
        if char_count[s[i]]==1:
            return i
    return -1


print(first_non_repeating_char('baknsb'))