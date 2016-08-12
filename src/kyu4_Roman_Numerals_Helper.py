class Solution():

    def __init__(self):
        self.RomanNumerals = self.RomanNumerals_01

    class RomanNumerals_01():

        @staticmethod
        def to_roman(num):
            int2roman_dict = \
                {
                    1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
                    40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
                    500: 'D', 900: 'CM', 1000: 'M',
                }
            ret = []
            for n in [1000, 1000, 1000, 900, 500, 400, 100, 100, 100, 90, 50, 40, 10, 10, 10, 9, 5, 4, 1, 1, 1]:
                if num >= n:
                    ret.append(int2roman_dict[n])
                    num -= n
            return ''.join(ret)

        @staticmethod
        def from_roman(s):
            roman2int_dict = \
                {
                    'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
                    'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400,
                    'D': 500, 'CM': 900, 'M': 1000,
                }
            len_s = len(s)
            i = 0
            num = 0
            for roman in ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']:
                while i < len_s and s.startswith(roman, i):
                    num += roman2int_dict[roman]
                    i += len(roman)
            return num


if __name__ == '__main__':
    sol = Solution()
    print(sol.RomanNumerals.from_roman('MDCLXVI'))
    print(sol.RomanNumerals.to_roman(1666))
