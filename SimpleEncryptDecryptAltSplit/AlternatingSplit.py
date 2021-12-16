def decrypt(encrypted_text, n):
    for i in range (0,n):
        firstHalf = []
        secondHalf = []
        text = ""
        count = 0
        count2 = 0
        for letter in encrypted_text:
            if count <= (len(encrypted_text)-1)/2:
                firstHalf.append(letter)
            else:
                secondHalf.append(letter)
            count += 1
        print(f"Second Half {secondHalf}")
        print(f"First Half {firstHalf}")
        while count2 <= count/2:
            try:
                text = text + secondHalf[count2] + firstHalf[count2]
            except:
                text = text
            count2 += 1
        encrypted_text = text
    return(text)


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
    return (text)

test = "This is a test"
test2 = "012345"
n = 3
comes_back = encrypt(test, n)
decrypt(comes_back, n)