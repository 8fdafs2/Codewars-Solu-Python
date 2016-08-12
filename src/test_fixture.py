class Test_Fixture():
    """
    """

    def __init__(self, sol, sets_gen, cmpr=None,
                 id_def=-1,
                 ids_test=[],
                 ids_test_spd=[]):

        name_subsols = [item for item in dir(sol) if item[:2] != '__']
        name_subsol_base = name_subsols[0][:-3]

        self.subsols = \
            [getattr(sol, name_subsol) for name_subsol in name_subsols]

        if id_def >= 0:
            self.subsol_def = getattr(
                sol, '{:s}_{:02d}'.format(name_subsol_base, id_def))
        else:
            self.subsol_def = self.subsols[0]

        if ids_test:
            self.subsols_test = \
                [getattr(sol, '{:s}_{:02d}'.format(name_subsol_base, id_test))
                 for id_test in ids_test]
        else:
            self.subsols_test = self.subsols

        if ids_test_spd:
            self.subsols_test_spd = \
                [getattr(sol, '{:s}_{:02d}'.format(name_subsol_base, id_test))
                 for id_test in ids_test_spd]
        else:
            self.subsols_test_spd = self.subsols

        self.sets_gen = sets_gen

        if cmpr:
            self.cmpr = cmpr
        else:
            def cmpr(to_match, test_set):
                return to_match == test_set[-1]
            self.cmpr = cmpr

        n_time = 10
        n_docstr = len('DocStr')
        for subsol in self.subsols:
            if subsol.__doc__:
                n_docstr = max(n_docstr, len(
                    ' '.join([l.strip() for l in subsol.__doc__.strip().split()])))
        n_name = max(map(len, name_subsols + ['SubSol', ]))
        self.tabfmt = [
            [
                '  --{:s}--'.format('-' * n_name),
                '    {{:{:d}s}}'.format(n_name).format('SubSol'),
                '  --{:s}--'.format('-' * n_name),
                '    {{:{:d}s}}'.format(n_name)
            ],
            [
                '  --{:s}---{:s}--'.format('-' *
                                           n_name, '-' * n_docstr),
                '    {{:{:d}s}} | {{:s}}'.format(
                    n_name).format('SubSol', 'DocStr'),
                '  --{:s}-+-{:s}--'.format('-' *
                                           n_name, '-' * n_docstr),
                '    {{:{:d}s}} | {{:s}}'.format(n_name)
            ],
        ]
        self.tabfmt_spd = [
            [
                '  --{:s}---{:s}--'.format('-' * n_name, '-' * n_time),
                '    {{:{:d}s}} | {{:>10s}}'.format(
                    n_name).format('SubSol', 'Time[s]'),
                '  --{:s}-+-{:s}--'.format('-' * n_name, '-' * n_time),
                '    {{:{:d}s}} | {{:10.6f}}'.format(n_name),
            ],
            [
                '  --{:s}---{:s}---{:s}--'.format(
                    '-' * n_name, '-' * n_time, '-' * n_docstr),
                '    {{:{:d}s}} | {{:>10s}} | {{:s}}'.format(
                    n_name).format('SubSol', 'Time[s]', 'DocStr'),
                '  --{:s}-+-{:s}-+-{:s}--'.format(
                    '-' * n_name, '-' * n_time, '-' * n_docstr),
                '    {{:{:d}s}} | {{:10.6f}} | {{:s}}'.format(n_name),
            ],
        ]

    def prep(self):
        print('>>> prep')
        self.test_sets = self.sets_gen(self.subsol_def)
        print('\t{} -> {} TestSets of Type(\n\t    #01: {},\n\t    #02: {},\n\t    #03: {}\n\t)'.format(
            self.subsol_def.__name__,
            len(self.test_sets),
            tuple(map(type, self.test_sets[0][0])),
            type(self.test_sets[0][1]) if len(self.test_sets[
                0]) == 2 else tuple(map(type, self.test_sets[0][1])),
            'None' if len(self.test_sets[0]) == 2 else type(
                self.test_sets[0][2]),
        )
        )
        print('<<< prep')

    def test(self, prt_docstr=True):
        print('>>> test')

        tabfmt = self.tabfmt[prt_docstr]
        print(tabfmt[0])
        print(tabfmt[1])
        print(tabfmt[2])

        for subsol in self.subsols_test:
            for test_set in self.test_sets:
                if len(test_set) == 2:
                    to_match = subsol(*test_set[0])
                elif len(test_set) == 3:
                    to_match = subsol(*test_set[0])(*test_set[1])
                else:
                    raise ValueError(
                        'the length of test_set should be either 2 or 3')

                try:
                    assert self.cmpr(to_match, test_set)
                except AssertionError:
                    print('\n\t------ !!! ' + subsol.__name__ + ' ------')
                    print('\tinput:\n\t\t{}'.format(test_set[0]))
                    if len(test_set) == 3:
                        print('\tinput (extra):\n\t\t{}'.format(test_set[1]))
                    print('\toutput:\n\t\texpect: {}\n\t\tactual: {}'.format(
                        test_set[-1], to_match))
                    print('\t-----------' + '-' *
                          len(subsol.__name__) + '-------\n')

            print(tabfmt[3].format(
                subsol.__name__,
                '' if not subsol.__doc__ else ' '.join(
                    [l.strip() for l in subsol.__doc__.strip().split()]),
            ))
        print(tabfmt[0])
        print('<<< test')

    def test_spd(self, _number_=100, prt_docstr=True):
        print('>>> test_spd')
        import timeit

        tabfmt_spd = self.tabfmt_spd[prt_docstr]
        print(tabfmt_spd[0])
        print(tabfmt_spd[1])
        print(tabfmt_spd[2])

        for subsol in self.subsols_test_spd:

            def f():
                for test_set in self.test_sets:
                    if len(test_set) == 2:
                        subsol(*test_set[0])
                    elif len(test_set) == 3:
                        subsol(*test_set[0])(*test_set[1])
                    else:
                        raise ValueError(
                            'the length of test_set should be either 2 or 3')

            t = timeit.Timer(f)

            print(tabfmt_spd[3].format(
                subsol.__name__,
                t.timeit(number=_number_),
                '' if not subsol.__doc__ else ' '.join(
                    [l.strip() for l in subsol.__doc__.strip().split()]),
            ))

        print(tabfmt_spd[0])
        print('<<< test_spd')


class Solution():
    def __init__(self):
        pass

    def sol_01(self, x):
        """
        2 * x
        """
        return 2 * x

    def sol_02(self, x):
        """
        x + x
        """
        return x + x

    def sol_03(self, x):
        """
        x << 1
        """
        return x << 1


def sets_gen(sol):
    test_sets = []
    for x in range(1000):
        test_sets.append((
            (x,),
            sol(x)
        ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(10000, prt_docstr=True)
