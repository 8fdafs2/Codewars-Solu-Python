from collections import Counter


class Solution():
    """
    https://www.codewars.com/kata/54da539698b8a2ad76000228

    You live in the city of Cartesia where all roads are laid out in a perfect grid.
    You arrived ten minutes too early to an appointment,
    so you decided to take the opportunity to go for a short walk.
    The city provides its citizens with a Walk Generating App on their phones --
    everytime you press the button
    it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
    You know it takes you one minute to traverse one city block,
    so create a function that will return true if the walk the app gives you will take you exactly ten minutes
    (you don't want to be early or late!) and will,
    of course, return you to your starting point. Return false otherwise.

    Note:
    you will always receive a valid array containing a random assortment of direction letters
        ('n', 's', 'e', or 'w' only).
    It will never give you an empty array (that's not a walk, that's standing still!).
    """

    def __init__(self):
        pass

    def isValidWalk_01(self, walk):
        """
        list.count
        """
        return (
            len(walk) == 10 and
            walk.count('e') == walk.count('w') and
            walk.count('s') == walk.count('n')
        )

    def isValidWalk_02(self, walk):
        """
        collections.Counter
        """
        if len(walk) != 10:
            return False
        c = Counter(walk)
        if c['e'] != c['w'] or c['s'] != c['n']:
            return False
        return True


def sets_gen(isValidWalk):
    import random
    walkdirs = ['e', 'w', 's', 'n']
    test_sets = []
    for i in range(1000):
        if random.choice((True, False)):
            walk = [random.choice(walkdirs) for _ in range(5)]
            c = Counter(walk)
            for j in range(5):
                walkdirs_cand = []

                if c['e'] > c['w']:
                    walkdirs_cand.append('w')
                elif c['e'] < c['w']:
                    walkdirs_cand.append('e')

                if c['s'] > c['n']:
                    walkdirs_cand.append('n')
                elif c['s'] < c['n']:
                    walkdirs_cand.append('s')

                if len(walkdirs_cand) == 0:
                    walkdirs_cand = walkdirs

                walkdir = random.choice(walkdirs_cand)
                c[walkdir] += 1
                walk.append(walkdir)
        else:
            walk = [random.choice(walkdirs) for _ in range(random.randrange(6, 14))]
        match = isValidWalk(walk)
        test_sets.append((
            (walk,),
            match
        ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(1000, prt_docstr=True)
