def decrypt(encrypted_text, n):
    for i in range (0,n):
        count = 0
        text = []
        for letter in encrypted_text:
            text.append(letter)
            if count < len(encrypted_text)/2:
                text[2*count + 1] = letter
            else:
                text[2*count - 14] = letter
            count += 1
        print(text)
    print(encrypted_text)
    return (encrypted_text)



def encrypt(text, n):
    for i in range (0,n):
        count = 1
        odd = ""
        even = ""
        for letter in text:
            if count % 2 != 0:
                even = even + letter
            else:
                odd = odd + letter
            count += 1
        text = odd + even
        print(text)
    return (text)

test = "This is a test"
n = 15
comes_back = encrypt(test, n)
decrypt(comes_back, n)