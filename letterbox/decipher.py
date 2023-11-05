
#takes in a SecretMessage object (form) when it is saved and creates an object of model EncryptedMessage.
#object to be passed in with .get(id=id)?
def decipher_message(message, keyword):
    msg = message
    # need to remove whitespace from keyword
    alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
    alpha_upper = alpha_lower.upper()
    k = -1
    c = -1
    decrypted = ''
    for char in msg:
        c += 1
        if char == '\n' or char == ' ':
            decrypted += char
        elif char in '1234567890':
            decrypted += char
        elif char in '";:,.?/()[]+=-_!@#$%^&*':
            decrypted += char
        else:
            k += 1
            if k == len(keyword):  # reset the k index
                k = 0
            if char in alpha_lower:
                mat_key = alpha_lower.index(char) - alpha_lower.index(keyword.lower()[k])
                if mat_key < 0:
                    mat_key += 26
                decrypted += alpha_lower[mat_key]
            elif char in alpha_upper:
                mat_key = alpha_upper.index(char) - alpha_upper.index(keyword.upper()[k])
                if mat_key < 0:
                    mat_key += 26
                decrypted += alpha_upper[mat_key]
    return decrypted
#print(cipher_message('meetmeontuesdayeveningatseven', 'vigilance'))
#print(cipher_message('m', 'vigilance'))
