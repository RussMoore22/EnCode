
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
        else:
            k += 1
            if k == len(keyword)-1:  # reset the k index
                k = 0
            if char in alpha_lower:
                try:
                    print(alpha_lower.index(char)+alpha_lower.index(keyword.lower()[k]))
                    encrypted += (alpha_lower[alpha_lower.index(char)+alpha_lower.index(keyword.lower()[k])])
                except:
                    encrypted += (alpha_lower[alpha_lower.index(char)+alpha_lower.index(keyword.lower()[k]) - 26])
                    print('uh oh')

            elif char in alpha_upper:
                try:
                    print(alpha_upper.index(char)+alpha_upper.index(keyword.upper()[k]))
                    encrypted += (alpha_upper[alpha_upper.index(char)+alpha_upper.index(keyword.lower()[k])])
                except:
                    encrypted += (alpha_upper[alpha_upper.index(char)+alpha_upper.index(keyword.lower()[k]) - 26])
                    print('uh oh')
    return encrypted
#print(cipher_message('meetmeontuesdayeveningatseven', 'vigilance'))
#print(cipher_message('m', 'vigilance'))
