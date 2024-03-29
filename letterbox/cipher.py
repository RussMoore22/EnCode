
#takes in a SecretMessage object (form) when it is saved and creates an object of model EncryptedMessage.
#object to be passed in with .get(id=id)?
def cipher_message(message, keyword):
    msg = message
    # need to remove whitespace from keyword
    alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
    alpha_upper = alpha_lower.upper()
    k = -1
    c = -1
    encrypted = ''
    for char in msg:
        c += 1
        if char == '\n' or char == ' ':
            encrypted += char
        elif char in '1234567890':
            encrypted += char
        elif char in '";:,.?/()[]+=-_!@#$%^&*':
            encrypted += char
        else:
            k += 1
            if k == len(keyword):  # reset the k index
                k = 0
            if char in alpha_lower:
                mat_key = alpha_lower.index(char)+alpha_lower.index(keyword.lower()[k])
                if mat_key >25:
                    mat_key -= 26
                encrypted += alpha_lower[mat_key]
            elif char in alpha_upper:
                mat_key = alpha_upper.index(char)+alpha_upper.index(keyword.upper()[k])
                if mat_key >25:
                    mat_key -= 26
                encrypted += alpha_upper[mat_key]
    return encrypted
#print(cipher_message('meetmeontuesdayeveningatseven', 'vigilance'))
#print(cipher_message('m', 'vigilance'))
