# Write a function to find the most frequent character in a string

# input='hello'
# output='l'

def most_frequent_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    
    max_char = ""
    max_count = 0
    
    for char,count in char_count.items():
        if count > max_count:
            max_char=char
            max_count=count
    
            
    return max_char,max_count

print(most_frequent_char('hello'))