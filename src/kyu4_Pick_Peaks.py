class Solution():
    """
    https://www.codewars.com/kata/pick-peaks

    In this kata, you will create an object that returns
    the positions and the values of the "peaks" (or local maxima) of a numeric array.

    For example, the array arr = [ 0 , 1 , 2 , 5 , 1 , 0 ] has a peak in position 3 with a value of 5 (arr[3] = 5)

    The output will be returned as an object with two properties: pos and peaks.
    Both of these properties should be arrays.
    If there is no peak in the given array, then the output should be {pos: [], peaks: []}.

    Example: pickPeaks([3,2,3,6,4,1,2,3,2,1,2,3]) returns {pos:[3,7],peaks:[6,3]}

    All input arrays will be valid numeric arrays (although it could still be empty),
    so you won't need to validate the input.

    The first and last elements of the array will not be considered as peaks
    (in the context of a mathematical function,
    we don't know what is after and before and therefore, we don't know if it is a peak or not).

    Also, beware of plateaus !!! [1,2,2,2,1] has a peak while [1, 2, 2, 2, 3] does not.
    In case of a plateau-peak, please only return the position and value of the beginning of the plateau.
    For example: pickPeaks([1,2,2,2,1]) returns {pos:[1],peaks:[2]}

    have fun!
    """

    def __init__(self):
        pass

    def pick_peaks_01(self, arr):
        """
        two slots (last trend before last trend, last trend) tracking list
        """
        if not arr:
            return {'pos': [], 'peaks': []}
        pos = []
        m = {'up': 1, 'plateau': 0, 'down': -1}
        ups_downs = [None, None]
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                ups_downs.append(m['up'])
            elif arr[i] == arr[i + 1]:
                if ups_downs[-1] == m['up']:
                    pos_peak = i
                if ups_downs[-1] != m['plateau']:
                    ups_downs.append(m['plateau'])
            else:
                if ups_downs[-1] == m['up']:
                    pos.append(i)
                elif ups_downs[-2] == m['up'] and ups_downs[-1] == m['plateau']:
                    pos.append(pos_peak)
                ups_downs.append(m['down'])

        return {'pos': pos, 'peaks': [arr[i] for i in pos]}

    def pick_peaks_02(self, arr):
        """
        tracking list, candidate pos recorded
        """
        if not arr:
            return {'pos': [], 'peaks': []}
        pos = []
        trends = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
        pos_candi = 0
        for i in range(len(trends)):
            if trends[i] > 0:
                pos_candi = i + 1
            elif trends[i] < 0:
                if pos_candi:
                    pos.append(pos_candi)
                pos_candi = 0

        return {'pos': pos, 'peaks': [arr[i] for i in pos]}

    def pick_peaks_03(self, arr):
        """
        tracking list, candidate pos integrated
        """
        if not arr:
            return {'pos': [], 'peaks': []}
        pos = []
        trends = list(filter(lambda x: x[1] != 0, [(i + 1, arr[i + 1] - arr[i]) for i in range(len(arr) - 1)]))
        for i in range(len(trends) - 1):
            if trends[i][1] > 0 > trends[i + 1][1]:
                pos.append(trends[i][0])

        return {'pos': pos, 'peaks': [arr[i] for i in pos]}

    def pick_peaks_04(self, arr):
        """
        single tracking var: {uphill: pos, downhill: None}
        """
        if not arr:
            return {'pos': [], 'peaks': []}
        pos = []
        prob_peak = None
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                prob_peak = i
            elif arr[i] < arr[i - 1] and prob_peak:
                pos.append(prob_peak)
                prob_peak = None

        return {'pos': pos, 'peaks': [arr[i] for i in pos]}

    def pick_peaks_05(self, arr):
        """
        search next different h every time
        """
        pos = []
        peaks = []
        for i in range(1, len(arr)):
            h_next_different = next((h for h in arr[i:] if h != arr[i]), 2147483647)
            if arr[i - 1] < arr[i] and h_next_different < arr[i]:
                pos.append(i)
                peaks.append(arr[i])
        return {'pos': pos, 'peaks': peaks}


def sets_gen(pick_peaks):
    import random
    test_sets = []
    for i in range(3, 300):
        arr = [random.randint(-5, 5) for _ in range(i)]
        match = pick_peaks(arr)
        test_sets.append((
            (arr,),
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
