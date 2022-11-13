import string

def alphanumeric(password):
    if password == "":
        return False
    else:
        valid = f"{string.ascii_letters}{string.digits}"
        for i in password:
            if i not in valid:
                return False
        return True
        
print(alphanumeric("Hello"))