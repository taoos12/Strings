def to_uppercase_string(s):
    result = ""
    for char in s:
        if 'a'<= char <= 'z':
            result +=chr(ord(char)-32)
        else:
            result += char
    return result

print(to_uppercase_string('hello')) 