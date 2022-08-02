LETTER_MIN = 65
LETTER_MAX = 90
LETTER_RANGE = range(LETTER_MIN, LETTER_MAX + 1)

NUMBER_MIN = 48
NUMBER_MAX = 57
NUMBER_RANGE = range(NUMBER_MIN, NUMBER_MAX + 1)

def caesar_encrypt(text, shift=3):
    text = text.upper()
    encrpyted = ""
    for c in text:
        o = ord(c)
        if o in LETTER_RANGE:
            pos = o - LETTER_MIN
            new_pos = (pos + shift) % 26
            new_c = chr(new_pos + LETTER_MIN)
            encrpyted += new_c
        else:
            encrpyted += c
    
    return encrpyted

def clean_text(text, with_space=True):
    text = text.upper()
    cleaned = ""
    for c in text:
        o = ord(c)
        if o in LETTER_RANGE or (o == 32 and with_space):
            cleaned += c
    
    return cleaned