# Code to decipher and return morse code

def decodeMorse(morse_code):

    # Dictionary for morse code
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', 'SOS':'...---...'}
    
    # Setting key and value lists
    key_list = list(MORSE_CODE_DICT.keys())
    val_list = list(MORSE_CODE_DICT.values())

    # Setting temporary and new variables
    human = ""
    temp = ""

    # Counter to keep track of multiple spaces
    count = 0
    for part in morse_code:
        if part != " ":
            temp = temp + part
            count = 0
        elif part == " " and count < 1:
            position = val_list.index(temp)
            morse = key_list[position]
            human = human + str(morse)
            temp = ""
            count += 1
        elif count < 2:
            count += 1
        else:
            human = human + " "
            count = 0

    if temp != "":
        position = val_list.index(temp)
        morse = key_list[position]
        human = human + str(morse)
    print(human)

decodeMorse('.... . -.--   .--- ..- -.. .')
decodeMorse('...---...')