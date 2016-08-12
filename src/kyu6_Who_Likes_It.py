class Solution():
    """
    https://www.codewars.com/kata/5266876b8f4bf2da9b000362

    You probably know the "like" system from Facebook and other pages.
    People can "like" blog posts, pictures or other items.
    We want to create the text that should be displayed next to such an item.

    Implement a function likes :: [String] -> String,
    which must take in input array,
    containing the names of people who like an item.
    It must return the display text as shown in the examples:

    likes [] // must be "no one likes this"
    likes ["Peter"] // must be "Peter likes this"
    likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
    likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
    likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"

    For more than 4 names, the number in and 2 others simply increases.
    """

    def __init__(self):
        pass

    def likes_01(self, names):
        """
        if-ret-if-ret-...
        """
        len_names = len(names)

        if len_names == 0:
            return 'no one likes this'
        if len_names == 1:
            return names[0] + ' likes this'
        if len_names == 2:
            return names[0] + ' and ' + names[1] + ' like this'
        if len_names == 3:
            return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'

        return names[0] + ', ' + names[1] + ' and ' + str(len_names - 2) + ' others like this'

    def likes_02(self, names):
        """
        map format, manually set
        """
        len_names = len(names)

        format_map = {
            0: 'no one likes this',
            1: '{0[0]} likes this',
            2: '{0[0]} and {0[1]} like this',
            3: '{0[0]}, {0[1]} and {0[2]} like this',
        }

        return format_map.get(len_names, '{{0[0]}}, {{0[1]}} and {0} others like this'.format(len_names - 2)).format(
            names, len_names - 2)

    def likes_03(self, names):
        """
        map format, automatically set
        """
        len_names = len(names)

        format_map = {
            0: 'no one likes this',
            1: '{} likes this',
            2: '{} and {} like this',
            3: '{}, {} and {} like this',
            4: '{}, {} and {n_others} others like this',
        }

        return format_map[len_names if len_names < 4 else 4].format(*names[0:3], n_others=len_names - 2)


def sets_gen(likes):
    import random
    letters = 'abcdefghijklmnopqrstuvwxyz'
    test_sets = []
    for i in range(100):
        names = [''.join([random.choice(letters) for _ in range(random.randrange(5, 8))]) for _ in
                 range(i)]
        match = likes(names)
        test_sets.append((
            (names,),
            match))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(1000, prt_docstr=True)
