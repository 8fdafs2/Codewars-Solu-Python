class Solution():
    """
    https://www.codewars.com/kata/542ea700734f7daff80007fc

    In this task you have to code process planner.

    You will be given initial thing,
    target thing and a set of processes to turn one thing into another
    (in the form of [process_name, start_thing, end_thing]).
    You must return names of shortest sequence of processes to turn initial thing into target thing,
    or empty sequence if it's impossible.

    If start already equals end, return [], since no path is required.

    Example:

    test_processes = [
        ['gather', 'field', 'wheat'],
        ['bake', 'flour', 'bread'],
        ['mill', 'wheat', 'flour']
    ];

    processes('field', 'bread', test_processes) # should return ['gather', 'mill', 'bake']
    processes('field', 'ferrari', test_processes) # should return []
    processes('field', 'field', test_processes) # should return [], since no processes are needed

    Good luck!

    """

    def __init__(self):
        pass

    def processes_01(self, start, end, processes):
        """
        hashtab x 2
        """
        process_of = {}
        product_of = {}

        for process_name, start_thing, end_thing in processes:
            process_of[start_thing] = process_name
            product_of[start_thing] = end_thing

        ret = []
        try:
            while start != end:
                ret.append(process_of[start])
                start = product_of[start]
        except KeyError:
            return []

        return ret

    def processes_02(self, start, end, processes):
        """
        hashtab x 1
        """
        process_n_product_of = {}

        for process_name, start_thing, end_thing in processes:
            process_n_product_of[start_thing] = (process_name, end_thing)

        ret = []
        try:
            while start != end:
                process, start = process_n_product_of[start]
                ret.append(process)
        except KeyError:
            return []

        return ret

    def processes_03(self, start, end, processes):
        """
        brute-force
        """
        queue = [([], start)]
        while queue:
            path, dest = queue.pop()
            if dest == end:
                return path
            queue += [[path + [p], e] for p, s, e in processes if s == dest]
        return []


def sets_gen(processes):
    import random
    things = 'ABCDEFGHIJKLMNOPQRSTUVWXY'
    others = things.lower()
    processes_ = []
    for start, end in zip('ABCDEFGHIJKLMNOPQRSTUVWXY', 'BCDEFGHIJKLMNOPQRSTUVWXYZ'):
        processes_.append([start + '->' + end, start, end])
    random.shuffle(processes_)
    test_sets = []
    for i in range(1000):
        if random.choice((True, False)):
            start = random.choice(things)
            end = random.choice(things[things.index(start):])
        else:
            start = random.choice(others)
            end = random.choice(others)
        match = processes(start, end, processes_)
        test_sets.append((
            (start, end, processes_),
            match
        ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(100, prt_docstr=True)
