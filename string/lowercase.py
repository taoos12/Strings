def to_lowercase_string(s):
    result = ""
    for char in s:
        if 'A'<= char <= 'Z':
            result +=chr(ord(char)+32)
        else:
            result += char
    return result

print(to_lowercase_string('hEllO')) 