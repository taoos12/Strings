# Write a function to find the longest word in a given string
# input = 'I love python programming'
# output = 'programming'

def longest_words(s):
    words = s.split()

    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word
    
    
    return longest


print(longest_words('I love python coding' ))