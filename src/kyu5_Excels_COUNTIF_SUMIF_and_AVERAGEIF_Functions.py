class Solution():
    """
    https://www.codewars.com/kata/excels-countif-sumif-and-averageif-functions

    Microsoft Excel provides a number of useful functions for counting, summing,
    and averaging values if they meet a certain criteria.
    Your task is to write three functions that work similarly to Excel's COUNTIF, SUMIF and AVERAGEIF functions.

    Specifications

    Each function will take the same two arguments:

    A list object containing values to be counted, summed, or averaged.
    A criteria in either an integer, float, or string
    Integer or float indicates equality
    Strings can indicate >, >=, <, <= or <> (use the Excel-style "Not equal to" operator) to a number (ex. ">=3").
    In the count_if function, a string without an operator indicates equality to this string.
    The tests will all include properly formatted inputs.
    The test cases all avoid rounding issues associated with floats.

    Examples

        count_if([1,3,5,7,9], 3)
        1

        count_if(["John","Steve","John"], "John")
        2

        sum_if([2,4,6,-1,3,1.5],">0")
        16.5

        average_if([99,95.5,0,83],"<>0")
        92.5

    Excel Function Documentation:

        COUNTIF
        SUMIF
        AVERAGEIF
    """

    def __init__(self):
        pass

    def subsol_01(self, args):
        """
        """
        ops = {
            '<>': lambda a, b: a != b,
            '>=': lambda a, b: a >= b,
            '<=': lambda a, b: a <= b,
            '>': lambda a, b: a > b,
            '<': lambda a, b: a < b,
        }

        ops_keys = ('<>', '>=', '<=', '>', '<')

        def criteria_parse(criteria):
            if isinstance(criteria, str):
                for key in ops_keys:
                    if criteria.startswith(key):
                        return ops[key], float(criteria[len(key):])
            return lambda a, b: a == b, criteria

        def count_if(values, criteria):
            _op_, _v_ = criteria_parse(criteria)
            return len([_op_(v, _v_) for v in values])

        def sum_if(values, criteria):
            _op_, _v_ = criteria_parse(criteria)
            return sum([v for v in values if _op_(v, _v_)])

        def average_if(values, criteria):
            _op_, _v_ = criteria_parse(criteria)
            _vs_ = [v for v in values if _op_(v, _v_)]
            if not _vs_:
                return 0
            return sum(_vs_) / len(_vs_)

        values_c, criteria_c, values_s, criteria_s, values_a, criteria_a = args
        return count_if(values_c, criteria_c), \
               sum_if(values_s, criteria_s), \
               average_if(values_a, criteria_a)


    def subsol_02(self, args):
        """
        """
        def parse(values, criteria):
            if str(criteria)[0] not in '<>':
                return [v for v in values if v == criteria]

            return eval('[v for v in values if v ' + criteria + ']')

        def count_if(values, criteria):
            return len(parse(values, criteria))

        def sum_if(values, criteria):
            return sum(parse(values, criteria))

        def average_if(values, criteria):
            r = parse(values, criteria)
            return float(sum(r)) / len(r)

        values_c, criteria_c, values_s, criteria_s, values_a, criteria_a = args
        return count_if(values_c, criteria_c), \
               sum_if(values_s, criteria_s), \
               average_if(values_a, criteria_a)
