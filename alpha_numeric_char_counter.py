# WAP to count number, consonant, vowels and special character in a given string

def get_chars_count(s):
    vowels = 0
    consonants = 0
    digits = 0
    special = 0
    
    for char in s:
        if 'a' <= char.lower() <= 'z':
            if char.lower() in 'aeiou':
                vowels += 1
            else:
                consonants += 1
        elif '0' <= char <= '9':
            digits += 1
        else:
            special += 1
            
    return vowels, consonants, digits, special

print(get_chars_count("abcde12345$%"))


