import re

def encrypt(plaintext, key):
    encrypted_text = ''

    alphabet = {
      0: 'a',
      1: 'b',
      2: 'c',
      3: 'd',
      4: 'e',
      5: 'f',
      6: 'g',
      7: 'h',
      8: 'i',
      9: 'j',
      10: 'k',
      11: 'l',
      12: 'm',
      13: 'n',
      14: 'o',
      15: 'p',
      16: 'q',
      17: 'r',
      18: 's',
      19: 't',
      20: 'u',
      21: 'v',
      22: 'w',
      23: 'x',
      24: 'y',
      25: 'z'
    }

    for char in plaintext:
        if re.match('[a-z]', char.lower()):
            letter_key = 0
            for k, v in alphabet.items():
                if v == char:
                    letter_key += k
            encrypted_text += alphabet[(letter_key + key) % 25]
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(ciphertext, key):
    return encrypt(ciphertext, -key)

print(encrypt('adam owada 1235 was here! ! lol', 30))
print(decrypt('fifr tcfif 1235 cfx mjwj! ! qtq', 30))