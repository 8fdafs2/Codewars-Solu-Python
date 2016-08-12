# 8 0 LOAD_CONST 1 (", line 8>)
# 3 MAKE_FUNCTION 0
# 6 STORE_DEREF 2 (openDoor)
#
# 16 9 LOAD_CONST 2 (", line 16>)
# 12 MAKE_FUNCTION 0
# 15 STORE_DEREF 1 (lineCount)
#
# 26 18 LOAD_CLOSURE 0 (deliverLine)
# 21 LOAD_CLOSURE 1 (lineCount)
# 24 LOAD_CLOSURE 2 (openDoor)
# 27 BUILD_TUPLE 3
# 30 LOAD_CONST 3 (", line 26>)
# 33 MAKE_CLOSURE 0
# 36 STORE_DEREF 0 (deliverLine)
#
# 30 39 LOAD_FAST 0 (arg)
# 42 LOAD_GLOBAL 0 (knock)
# 45 COMPARE_OP 2 (==)
# 48 POP_JUMP_IF_FALSE 65
#
# 31 51 LOAD_CONST 4 ('"Knock knock."')
# 54 PRINT_ITEM
# 55 PRINT_NEWLINE
#
# 32 56 LOAD_CONST 5 ("Who's there?")
# 59 PRINT_ITEM
# 60 PRINT_NEWLINE
#
# 33 61 LOAD_DEREF 0 (deliverLine)
# 64 RETURN_VALUE
# >> 65 LOAD_CONST 0 (None)
# 68 RETURN_VALUE
# None

import random
import string

lineCountVar = 0


def knock(arg):
    def openDoor():
        global success
        success = ''.join(random.choice(string.ascii_uppercase) for _ in range(16))
        globals()[success] = True
        print('')
        print('Groan. That\'s the worst "knock knock" joke I\'ve ever heard.')
        print("Oh well, I suppose you'd better come in.")
        print('Welcome to the annual meeting of the Knock Knock Joke Society.')

    def lineCount():
        global lineCountVar
        lineCountVar += 1
        if lineCountVar == 1:
            print('"Harry."')
            print('Harry who?')
        if lineCountVar == 2:
            print('"Harry up and open the door, it\'s cold out here!"')
        return lineCountVar

    def deliverLine():
        if lineCount() == 2:
            openDoor()
        return deliverLine

    if arg == knock:
        print('"Knock knock."')
        print("Who's there?")
        return deliverLine
    return None


import inspect
import dis


class Solution():
    def __init__(self):
        self.sol = self.sol_01

    def sol_01(self):
        print('Is knock a func?')
        print((inspect.isfunction(knock)))

        ret = knock('knock')

        print('The ret type is:')
        print((type(ret)))
        print('Does the func return None?')
        print((ret is None))
        print('Check func\'s argspec:')
        print((inspect.getargspec(knock)))
        print('Print the byte code:')
        print('--------------------------')
        print((dis.dis(knock)))
        print('--------------------------')
        print('Seems the arg is compared with the func itself')
        print('Try pass the func itself in:')

        ret = knock(knock)

        print('The ret is:')
        print(ret)
        print('Inspect the ret\'s inner properties:')
        print((dir(ret)))
        print('Try call it since its callable:')

        ret_ret = knock(knock)()

        print('The ret_ret is:')
        print(ret_ret)
        print('Inspect the ret_ret\' attributes:')
        print((dir(ret_ret)))
        print('Try call it since its callable:')

        ret_ret_ret = knock(knock)()()

    def sol_02(self):
        global success
        success = 'a'
        a = True

    def sol_03(self):
        print(locals())
        print()
        print(dis.dis(knock))
        print()
        print(knock.__code__.co_consts[1].co_name)
        print(dis.dis(knock.__code__.co_consts[1]))
        print()
        print(knock.__code__.co_consts[2].co_name)
        print(dis.dis(knock.__code__.co_consts[2]))
        print()
        print(knock.__code__.co_consts[3].co_name)
        print(dis.dis(knock.__code__.co_consts[3]))
        print()

        knock(knock)()()


if __name__ == '__main__':
    sol = Solution()
    sol.sol_01()

    if not ('success' in globals()) and (globals()[globals()['success']] == True):
        print("Sorry, that's not the secret knock.")
