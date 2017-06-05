import pyperclip
import sys

class Cipher:
    def __init__(self, mode, message):
        pass

        self.message = message
        self.mode = mode

        self.key = 13

        self.LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.translated = ''
        self.message = self.message.upper()

        for symbol in self.message:
            if symbol in self.LETTERS:
                num = self.LETTERS.find(symbol)
                print(num)
                if mode == 'encrypt':
                    num = num + self.key
                elif mode == 'decrypt':
                    num = num - self.key

                if num >= len(self.LETTERS):
                    num = num - len(self.LETTERS)
                elif num < 0:
                    num = num + len(self.LETTERS)

                self.translated = self.translated + self.LETTERS[num]

            else:
                self.translated = self.translated + symbol

if __name__ == '__main__':
    mode = input('Type \'encrypt\' or \'decrypt\': ')
    if mode == 'encrypt':
        message = input('Encrypt: ')
        cipher = Cipher(mode, message)
    elif mode == 'decrypt':
        message = input('Decrypt: ')
        cipher = Cipher(mode, message)

    saveMsg = cipher.message.lower().replace(' ', '_')
    saveTranslate = cipher.translated.lower().replace(' ', '_')

    with open(cipher.mode + '-' + saveMsg + '-' + saveTranslate + '.txt', 'w') as archive:
        archive.write('%s\n//\n%s' % (cipher.message, cipher.translated))
        archive.close()
