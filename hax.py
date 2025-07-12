# https://sio2.mimuw.edu.pl/c/oij14-1/p/hax/

symbols = {
    'a': '4',
    'e': '3',
    's': '5',
    'o': '0',
    'i': '1'
}


def translate(text):
    letters = list(symbols)
    for letter in letters:
        text = text.replace(letter, symbols[letter])
    return text


print(translate("haker"))
