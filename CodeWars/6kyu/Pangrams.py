import string

def is_pangram(s):
    letters = string.ascii_lowercase
    exclude = string.punctuation
    s = s.lower()
    s = ''.join(ch for ch in s if ch not in exclude)
    
    for letter in s:
        if letter in letters:
            letters = letters.replace(letter, "")
    
    if letters == "":
        return True
    else:
        return False

pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram))