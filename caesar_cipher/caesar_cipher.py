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


def code_breaker(ciphertext, key):
    guessed_key = 0
    largest_tracker = 0
    with open('./wordlist_10000.txt', 'r') as dictionary:
        for i in range(2):
            tracker = 0
            for cipher_word in ciphertext.split():
                print(cipher_word)
                print(decrypt(cipher_word, i))
                for word in dictionary:
                    if word == f'{decrypt(cipher_word, i)}':
                        tracker += 1
            print(f'for key: {i}, the tracker is {tracker}')
            if tracker > largest_tracker:
                largest_tracker = tracker
                guessed_key = i
    if guessed_key == key:
        print(f'The computer guessed the key correctly. The key was {key}. The guessed key was {guessed_key}. The ciphertext was {ciphertext}. The plaintext was {decrypt(ciphertext, key)}.')
        return
    else:
        print('The computer guessed the wrong key.')
        return    


def split_check(sentence):
    for i in sentence.split():
        print(i)
    for i in range(26):
        print(i)

# print(encrypt('adam owada 1235 was here! ! lol', 30))
# print(decrypt('fifr tcfif 1235 cfx mjwj! ! qtq', 30))

# code_breaker('house')

# split_check('asdfa asdfa ddd asd eee.')

print(encrypt('house boat car dog cat liter', 1))
code_breaker('ipvtf cpbu dbs eph dbu mjufs', 1)