MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',

    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',

    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
    '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@',

    '...---...': 'SOS'
}


class Solution():
    def __init__(self):
        self.decodeBits = self.decodeBits_01
        self.decodeMorse = self.decodeMorse_01

    def decodeBits_01(self, bits):
        bits = bits.strip('0')
        unit_l = min([len(s) for s in bits.split('1') + bits.split('0') if s])

        return bits.replace(
            '111' * unit_l, '-').replace(
            '1' * unit_l, '.').replace(
            '0000000' * unit_l, '   ').replace(
            '000' * unit_l, ' ').replace(
            '0' * unit_l, '')

    def decodeMorse_01(self, morseCode):
        return ' '.join(
            [''.join([MORSE_CODE[letter] for letter in word.split(' ')]) for word in morseCode.strip().split('   ')])


if __name__ == '__main__':
    sol = Solution()

    morseCode = sol.decodeBits(('11001100110011000000110000001111110011001111110011111100000000000000'
                                '11001111110011111100111111000000110011001111110000001111110011001100000011'))
    print(repr(morseCode))
    print(sol.decodeMorse(morseCode))
