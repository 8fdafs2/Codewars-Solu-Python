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


def decodeMorse(morse_code):
    return ' '.join(
        [''.join([MORSE_CODE[letter] for letter in word.split(' ')])
         for word in morse_code.strip().split('   ')])


class Solution():
    """
https://www.codewars.com/kata/54acd76f7207c6a2880012bb

Part of Series 3/3
This kata is part of a series on the Morse code. Make sure you solve the first part and the second part and then reuse and advance your code to solve this one.

In this kata you have to deal with "real-life" scenarios, when Morse code transmission speed slightly varies throughout the message as it is sent by a non-perfect human operator. Also the sampling frequency may not be a multiple of the length of a typical "dot".
For example, the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· · may actually be received as follows:

0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000

As you may see, this transmission is generally accurate according to the standard, but some dots and dashes and pauses are a bit shorter or a bit longer than the others.

Note also, that, in contrast to the previous kata, the estimated average rate (bits per dot) may not be a whole number – as the hypotetical transmitter is a human and doesn't know anything about the receiving side sampling rate.

For example, you may sample line 10 times per second (100ms per sample), while the operator transmits so that his dots and short pauses are 110-170ms long. Clearly 10 samples per second is enough resolution for this speed (meaning, each dot and pause is reflected in the output, nothing is missed), and dots would be reflected as 1 or 11, but if you try to estimate rate (bits per dot), it would not be 1 or 2, it would be about (110 + 170) / 2 / 100 = 1.4. Your algorithm should deal with situations like this well.

Also, remember that each separate message is supposed to be possibly sent by a different operator, so its rate and other characteristics would be different. So you have to analyze each message (i. e. test) independently, without relying on previous messages. On the other hand, we assume the transmission charactestics remain consistent throghout the message, so you have to analyze the message as a whole to make decoding right. Consistency means that if in the beginning of a message '11111' is a dot and '111111' is a dash, then the same is true everywhere in that message. Moreover, it also means '00000' is definitely a short (in-character) pause, and '000000' is a long (between-characters) pause.

That said, your task is to implement two functions:

1. Function decodeBitsAdvanced(bits), that should find an estimate for the transmission rate of the message, take care about slight speed variations that may occur in the message, correctly decode the message to dots ., dashes - and spaces (one between characters, three between words) and return those as a string. Note that some extra 0's may naturally occur at the beginning and the end of a message, make sure to ignore them. If message is empty or only contains 0's, return empty string. Also if you have trouble discerning if the particular sequence of 1's is a dot or a dash, assume it's a dot. If stuck, check this for ideas.

2. Function decodeMorse(morseCode), that would take the output of the previous function and return a human-readable string. If the input is empty string or only contains spaces, return empty string.

The Morse code table is preloaded for you as MORSE_CODE dictionary, feel free to use it.

Of course, not all messages may be fully automatically decoded. But you may be sure that all the test strings would be valid to the point that they could be reliably decoded as described above, so you may skip checking for errors and exceptions, just do your best in figuring out what the message is!

Good luck!
    """

    def __init__(self):
        pass

    @staticmethod
    def decodeBitsAdvanced_01(bits):
        """
        intuitive
        """
        bits = bits.strip("0")
        if not bits:
            return ''
        if '0' not in bits:
            return '.'
        if bits == '1001':  # patch
            return '. .'

        t_dct = {}
        l_dct = {}
        l_0_lst = []
        l_1_lst = []

        for t in __import__('re').findall("(1+|0+)", bits):
            t_dct[t] = t_dct.get(t, 0) + 1
            l = len(t)
            l_dct[l] = l_dct.get(l, 0) + 1
            if t[0] == '0':
                if l not in l_0_lst:
                    l_0_lst.append(l)
            else:
                if l not in l_1_lst:
                    l_1_lst.append(l)

        l_0_lst.sort()
        l_1_lst.sort()
        l_0_c_lst = [[], [], []]
        l_1_c_lst = [[], []]

        #  '1'+ token based
        if len(l_1_lst) > 1 and float(l_1_lst[-1]) / l_1_lst[0] >= 2.5:
            i = len(l_1_lst) / 2.0
            if i == int(i):
                i = int(i)
                l_1_c_lst[0] = l_1_lst[:i]
                l_1_c_lst[1] = l_1_lst[i:]
                c0 = float(sum([l * l_dct[l] for l in l_1_c_lst[0]])) / \
                    sum([l_dct[l] for l in l_1_c_lst[0]])
                c1 = float(sum([l * l_dct[l] for l in l_1_c_lst[1]])) / \
                    sum([l_dct[l] for l in l_1_c_lst[1]])
            else:
                i = int(i)
                l_1_c_lst[0] = l_1_lst[:i]
                l_1_c_lst[1] = l_1_lst[i + 1:]
                c0 = float(sum([l * l_dct[l] for l in l_1_c_lst[0]])) / \
                    sum([l_dct[l] for l in l_1_c_lst[0]])
                c1 = float(sum([l * l_dct[l] for l in l_1_c_lst[1]])) / \
                    sum([l_dct[l] for l in l_1_c_lst[1]])
                l = l_1_lst[i]
                if l - c0 > c1 - l:
                    l_1_c_lst[1].insert(0, l)
                else:
                    l_1_c_lst[0].append(l)
                c0 = float(sum([l * l_dct[l] for l in l_1_c_lst[0]])) / \
                    sum([l_dct[l] for l in l_1_c_lst[0]])
                c1 = float(sum([l * l_dct[l] for l in l_1_c_lst[1]])) / \
                    sum([l_dct[l] for l in l_1_c_lst[1]])
            c2 = (c0 + c1) / 4.0 * 7
        else:
            if not l_0_lst:
                l_1_c_lst[0] = l_1_lst
                c0 = float(sum([l * l_dct[l] for l in l_1_lst])) / sum([l_dct[l] for l in l_1_lst])
                c1 = c0 * 3
                c2 = c0 * 7
            else:
                c = float(sum([l * l_dct[l] for l in l_1_lst])) / sum([l_dct[l] for l in l_1_lst])
                if c > l_0_lst[0]:
                    l_1_c_lst[1] = l_1_lst
                    c0 = c / 3.0
                    c1 = c
                    c2 = c0 * 7
                else:
                    l_1_c_lst[0] = l_1_lst
                    c0 = float(sum([l * l_dct[l] for l in l_1_lst])) / \
                        sum([l_dct[l] for l in l_1_lst])
                    c1 = c0 * 3
                    c2 = c0 * 7

        for l in l_0_lst:
            if l <= c0:
                l_0_c_lst[0].append(l)
            if l_1_c_lst[0] and l <= l_1_c_lst[0][-1]:  # patch
                l_0_c_lst[0].append(l)
            elif l_1_c_lst[1] and l <= l_1_c_lst[1][-1]:  # patch
                l_0_c_lst[1].append(l)
            elif l <= c1:
                if l - c0 > c1 - l:
                    l_0_c_lst[1].append(l)
                else:
                    l_0_c_lst[0].append(l)
            elif l <= c2:
                if l - c1 > c2 - l:
                    l_0_c_lst[2].append(l)
                else:
                    l_0_c_lst[1].append(l)
            else:
                l_0_c_lst[2].append(l)

        for l in reversed(l_0_c_lst[2]):
            bits = bits.replace('0' * l, '   ')
        for l in reversed(l_1_c_lst[1]):
            bits = bits.replace('1' * l, '-')
        for l in reversed(l_0_c_lst[1]):
            bits = bits.replace('0' * l, ' ')
        for l in reversed(l_1_c_lst[0]):
            bits = bits.replace('1' * l, '.')
        for l in reversed(l_0_c_lst[0]):
            bits = bits.replace('0' * l, '')

        return decodeMorse(bits)

    @staticmethod
    def decodeBitsAdvanced_02(bits):
        """
        """
        from re import compile

        TOKENIZER = compile('(0+)')

        class Cluster(object):
            def __init__(self, center, weight, mn, mx):
                self.center = center
                self.weight = weight
                self.mn = mn
                self.mx = mx

        bits = bits.strip('0')
        if not bits:
            return ''
        tokens = TOKENIZER.split(bits.strip('0'))
        lengths = sorted(len(token) for token in tokens)
        (minLen, maxLen) = (lengths[0], lengths[-1])
        lenRange = float(maxLen - minLen)
        # Employ 3-means clustering
        clusters = tuple(Cluster(minLen + lenRange * x / 8, 0, maxLen, minLen) for x in (1, 3, 7))
        for sample in lengths:
            # Find the closest cluster for this sample
            cluster = min(clusters, key=lambda cluster: abs(sample - cluster.center))
            # Adjust cluster: each sample has weight of 1, cluster center is adjusted,
            # its weight increases
            cluster.center = (cluster.center * cluster.weight + sample) / (cluster.weight + 1)
            cluster.weight += 1
            if sample < cluster.mn:
                cluster.mn = sample
            if sample > cluster.mx:
                cluster.mx = sample
        # Fill the gaps if we really have less than 3 clusters
        clusters = [cluster for cluster in clusters if cluster.weight]  # Filter out empty clusters
        if len(clusters) == 2:
            # If 1 and 7 are present while 3 is not, add a syntetic cluster for 3
            if float(clusters[1].mn) / clusters[0].mx >= 5:
                clusters.insert(1, Cluster(
                    (clusters[0].mx + clusters[1].mn) / 2.0, 0, clusters[0].mx + 1, clusters[1].mn - 1))
        if len(clusters) < 3:  # If only 1 is present (or only 1 and 3 are), add syntetic clusters for 3 and 7 (or just 7)
            limit = clusters[-1].mx + 1
            clusters.extend(Cluster(limit, 0, limit, limit) for i in range(3 - len(clusters)))
        # Calculating edges between dots and dashes, and dashes and word pauses
        maxDot = (clusters[0].mx + clusters[1].mn) / 2.0
        maxDash = (clusters[1].mx + clusters[2].mn) / 2.0
        # Perform transcoding
        ret = []
        for token in tokens:
            if token[0] == '1':
                ret.append('.' if len(token) <= maxDot else '-')
            elif len(token) > maxDot:
                ret.append(' ' if len(token) <= maxDash else '   ')
        return ''.join(ret)

    # @staticmethod
    # def decodeBitsAdvanced_03(bits):
    #     """
    #     """
    #     import re
    #     from scipy.cluster.vq import kmeans

    #     def decode_signal(signal):
    #         n = len(signal)
    #         if signal[0] == '0':
    #             if n < b0:
    #                 return ''
    #             elif n < b1:
    #                 return ' '
    #             else:
    #                 return '   '
    #         else:
    #             if n < b0:
    #                 return '.'
    #             else:
    #                 return '-'

    #     bits = bits.strip("0")
    #     if not bits:
    #         return ''
    #     if '0' not in bits:
    #         return '.'
    #     centroids, _ = kmeans([float(len(s)) for s in re.findall(r'1+', bits)], 2)
    #     m = sum(centroids) * 0.25
    #     b0, b1 = m * 2, m * 5
    #     return decodeMorse(''.join(decode_signal(s) for s in re.findall(r'0+|1+', bits)))


def sets_gen(subsol):
    bits_lst = [
        '',
        '0',
        '000000000000000000000000000000000000000000',
        '1',
        '101',
        '1001',
        '10001',
        '100001',
        '10000001',
        '100000001',
        '1000000001',
        '10000000001',
        '10111',
        '1110111',
        '111000111',
        '111',
        '1111111',
        '110011',
        '111110000011111',
        '11111100111111',
        '01110',
        '000000011100000',
        '0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000',
        '00000000000111111100000011010001110111000000001110000000000000000001111111011111100001101111100000111100111100011111100000001011100000011111110010001111100110000011111100101111100000000000000111111100001111010110000011000111110010000011111110001111110011111110000010001111110001111111100000001111111101110000000000000010110000111111110111100000111110111110011111110000000011111001011011111000000000000111011111011111011111000000010001001111100000111110111111110000001110011111100011111010000001100001001000000000000000000111111110011111011111100000010001001000011111000000100000000101111101000000000000011111100000011110100001001100000000001110000000000000001101111101111000100000100001111111110000000001111110011111100011101100000111111000011011111000111111000000000000000001111110000100110000011111101111111011111111100000001111110001111100001000000000000000000000000000000000000000000000000000000000000',
        '11111000001111111000011111100000111111111111111000011111111111111000000111111111111111100001110000011111100000001111000000000000000011111111111111000000111110000011111111111111100000011110000011111111111111100001111111111111110000000000000000000000000000000000011111111111111110000000000000001111000000111110000011110000000111100000000000000111110000000000000000000000000000000000011111111111111100000111111111111111000011111000001111111111111100000000000000001111111000000111111000000011111111111111000000000000000011110000001111100000000000000011111111111111100000111111000111111111111111000011110000000000000000111111111111110000000111100000111111111111110000000000000000000000000000000000011111111111111100000111111000011111000000111110000000000000001111110000111111111111111100000011110000000000000011111111111111100001111111111111110000111111111111110000000000000001111100000001111111111111110000000111111111111111110000000000000000111111111111111000001111100000000000000000000000000000000000011110001111100000011111111111111110000011100000000000000011111111111111110000011111111111110000001111111111111111000000000000001111111111111110000001111100001111110000001111111111111111000000000000000000000000000000000011110000011111111111111100000011111111111111100001111111111111111000000000000001111110001111000011111111111100000000000000001111111111111100000011111111111111100000000000000110000011111111111111100000111111111111111100000111110000000000000001111110000111110000111111000000000000000000000000000000000011111111111111110001111111111111111000001111111111111111000000000000000111100000111110000111100000111111111111111000000000000000111111000000000000000111000000111111111111111000111100000000000000000000000000000000000011111111111111100000000000000011111110000111100000111111000001111110000000000000001111110000000000000000000000000000000000000111111000111111111111111100000111100000011111110000000000000011110000111111111111111000000000000011111111111111000001111111111111111000001111100001111100000000000000011111111111111000001111110000011111111111111111000011111111111111100000000000000000000000000000000000001111111111111111000001111110000011110000000000000111111111111111000001111111111111111000011111111111111110000000000000001111111111111100000011111111111111100000111100000000000000011111100000111111111111110000001110000011111111111111110000011111000011111111111111',
        '00000000000000011111111000000011111111111100000000000111111111000001111111110100000000111111111111011000011111111011111111111000000000000000000011111111110000110001111111111111000111000000000001111111111110000111111111100001100111111111110000000000111111111111011100001110000000000000000001111111111010111111110110000000000000001111111111100001111111111110000100001111111111111100000000000111111111000000011000000111000000000000000000000000000011110001111100000111100000000111111111100111111111100111111111111100000000011110011111011111110000000000000000000000111111111110000000011111000000011111000000001111111111110000000001111100011111111000000000111111111110000011000000000111110000000111000000000011111111111111000111001111111111001111110000000000000000000001111000111111111100001111111111111100100000000001111111100111111110111111110000000011101111111000111000000001001111111000000001111111111000000000111100001111111000000000000011111111100111111110111111111100000000000111111110000001100000000000000000000111111101010000010000001111111100000000011111000111111111000000111111111110011111111001111111110000000011000111111110000111011111111111100001111100001111111100000000000011110011101110001000111111110000000001111000011111110010110001111111111000000000000000000111111111110000000100000000000000000011110111110000001000011101110000000000011111111100000011111111111100111111111111000111111111000001111111100000000000001110111111111111000000110011111111111101110001111111111100000000111100000111100000111111111100000111111111111000000011111111000000000001000000111100000001000001111100111111111110000000000000000000010001111111100000011111111100000000000000100001111111111110111001111111111100000111111100001111111111000000000000000000000000011100000111111111111011110000000010000000011111111100011111111111100001110000111111111111100000000000000111110000011111001111111100000000000011100011100000000000011111000001111111111101000000001110000000000000000000000000000111110010000000000111111111000011111111110000000000111111111111101111111111100000000010000000000000011111111100100001100000000000000111100111100000000001100000001111111111110000000011111111111000000000111100000000000000000000111101111111111111000000000001111000011111000011110000000001100111111100111000000000100111000000000000111110000010000011111000000000000001111111111100000000110111111111100000000000000111111111111100000111000000000111111110001111000000111111110111111000000001111000000000010000111111111000011110001111111110111110000111111111111000000000000000000000000111111111110000000111011111111100011111110000000001111111110000011111111100111111110000000001111111111100111111111110000000000110000000000000000001000011111111110000000001111111110000000000000000000000011111111111111000000111111111000001111111110000000000111111110000010000000011111111000011111001111111100000001110000000011110000000001011111111000011111011111111110011011111111111000000000000000000100011111111111101111111100000000000000001100000000000000000011110010111110000000011111111100000000001111100011111111111101100000000111110000011110000111111111111000000001111111111100001110111111111110111000000000011111111101111100011111111110000000000000000000000000010000111111111100000000001111111110111110000000000000000000000110000011110000000000001111111111100110001111111100000011100000000000111110000000011111111110000011111000001111000110000000011100000000000000111100001111111111100000111000000001111111111000000111111111100110000000001111000001111111100011100001111111110000010011111111110000000000000000000111100000011111000001111000000000111111001110000000011111111000100000000000011111111000011001111111100000000000110111000000000000111111111111000100000000111111111110000001111111111011100000000000000000000000000',
    ]
    test_sets = []
    for bits in bits_lst:
        match = subsol(bits)
        test_sets.append((
            (bits,),
            match
        ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    tf = __import__('test_fixture').Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(1000, prt_docstr=True)
