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
    def decodeBitsAdvanced_01(n):
        """
        """
        return


def sets_gen(subsol):
    import random
    test_sets = []
    for n in range(1000):
        match = subsol(random.randint(0, 100))
        test_sets.append((
            (n,),
            match
        ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(10, prt_docstr=True)
