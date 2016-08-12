class OrderedDictWithRepeatableKey_01():

    def __init__(self):
        self.keylst = []
        self.i_keylst = -1

    def __setitem__(self, key, value):
        self.keylst.append((key, value))

    def __getitem__(self, key):
        self.i_keylst = (self.i_keylst + 1) % len(self.keylst)
        while self.keylst[self.i_keylst][0] != key:
            self.i_keylst = (self.i_keylst + 1) % len(self.keylst)
        return self.keylst[self.i_keylst][1]

    def __iter__(self):
        return (key[0] for key in self.keylst)

    def keys(self):
        return list(self)

    def iteritems(self):
        return ((key[0], self.__getitem__(key[0])) for key in self.keylst)

    def items(self):
        return list(self.iteritems())


class OrderedDictWithRepeatableKey_02(object):

    def __init__(self):
        self.pairs = []
        self.wrapped = {}

    def wrap(self, what, idx):
        T = type(what)
        if T not in self.wrapped:
            self.wrapped[T] = type(T.__name__, (T,), {})
        w = self.wrapped[T](what)
        w._idx = idx
        return w

    def __setitem__(self, key, value):
        idx = len(self.pairs)
        self.pairs.append((self.wrap(key, idx), value))

    def __getitem__(self, key):
        try:
            idx = key._idx
        except AttributeError:
            idx = self.keys().index(key)
        return self.pairs[idx][1]

    iteritems = lambda self: (pair for pair in self.pairs)
    __iter__ = lambda self: (key for key, value in self.pairs)
    keys = lambda self: list(self)
    items = lambda self: list(self.iteritems())


def fill(d):
    """ Solve without touching this! """
    d[1] = 10
    d[2] = 20
    d[1] = 30
    d[2] = 40


class Solution():
    """
    https://www.codewars.com/kata/list-of-pairs-instead-of-dictionary/train/python

    You work with a legacy code base which you don't have access to modify.

    Once you just spot a discrepancy in a particular legacy function fill that
    fills up the dictionary d - given as its argument - by thousands of commands like

    d[key] = value

    The problem is that the particular key you have to work with appears multiple times as key in the fill function,
    and of course you need to handle each belonging value, not just the last one.

    Luckily you have access to the initialization of this dictionary,
    the method called the_dict, which invokes this fill method.

    Your task is to hack the_dict so that the values for multiple keys in the result are
    all available when looping through the result 'dictionary'.

    You have checked through the legacy code,
    and after its initialization the result dictionary d is only used in one of the following contexts:

        use(d[key]) for a particular key
        for key in d: use(key,d[key])
        for key in d.keys(): use(key,d[key])
        for key,value in d.iteritems(): use(key,value)

    In the first case, any corresponding value d[key] will be accepted,
    but the loops are required to parse through the whole intended 'dictionary' -
    including the multiple keys - in the original order as d was filled in method fill.

    Note that the keys are integers or strings and might also be used in any numeric/string operation within the loop.
    Example

    Supposed that the untouchable fill is

    def fill(d):
        d[1] = 10
        d[2] = 20
        d[1] = 30
        d[2] = 40

    this loop should produce the following output:

    # >>> d = the_dict() # find in working panel
    # >>> for key in d:
    # ...     print key, d[key]
    1 10
    2 20
    1 30
    2 40
    """

    def __init__(self):
        pass

    def the_dict_01(self):
        """
        """
        d = OrderedDictWithRepeatableKey_02()
        d[8] = 10
        d['d'] = 'ss'
        d[2] = 9
        d[2] = 10
        d['d'] = 'ssss'

        print(d[2])
        print(d[2])

        for key in d:
            print(key, d[key])

        for key, value in d.items():
            print(key, value)

        for key in d.keys():
            print(key, d[key])


if __name__ == '__main__':
    sol = Solution()
    print(sol.the_dict_01())
