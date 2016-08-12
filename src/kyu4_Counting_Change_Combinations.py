class Solution():
    """
    Write a function that counts how many different ways you can make change for an amount of money,
    given an array of coin denominations.
    For example, there are 3 ways to give change for 4 if you have coins with denomination 1 and 2:

    1+1+1+1, 1+1+2, 2+2.

    The order of coins does not matter:

    1+1+2 == 2+1+1

    Also, assume that you have an infinite ammount of coins.

    Your function should take an amount to change and an array of unique denominations for the coins:

      count_change(4, [1,2]) # => 3
      count_change(10, [5,2,3]) # => 4
      count_change(11, [5,7]) # => 0
    """

    def __init__(self):
        pass

    def count_change_01(self, money, coins):
        """
        recursion, divmod
        """
        def recur(money, coins):
            ret = 0
            len_coins = len(coins)
            if len_coins == 0 or money == 0:
                return ret
            for j in range(len_coins):
                coin = coins[j]
                if money < coin:
                    return ret
                n, rest = divmod(money, coin)
                if rest == 0:
                    ret += 1
                    rng = range(n - 2)
                else:
                    rng = range(n - 1)
                _coins_ = coins[j + 1:]
                _money_ = money
                for i in rng:
                    _money_ -= coin
                    ret += recur(_money_, _coins_)
            return ret

        return recur(money, sorted(coins))

    def count_change_02(self, money, coins):
        """
        recursion, at least one of certain coin + no such coin at all
        """
        def recur(money, coins):
            if money < 0 or not coins:
                return 0
            if money == 0:
                return 1
            return recur(money - coins[-1], coins) + recur(money, coins[:-1])

        return recur(money, sorted(coins))

    def count_change_03(self, money, coins):
        """
        recursion by for-loop via list
        """
        dp = [1] + [0] * money
        for coin in coins:
            for x in range(coin, money + 1):
                dp[x] += dp[x - coin]

        return dp[money]



def sets_gen(count_change):
    import random
    test_sets = []
    for i in range(100):
        money = random.randint(21, 42)
        coins = [random.randint(1, 5)]
        for j in range(random.randint(3, 9)):
            coins.append(coins[-1] + random.randint(1, 5))
        random.shuffle(coins)
        match = count_change(money, coins)
        test_sets.append((
            (money, coins),
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
