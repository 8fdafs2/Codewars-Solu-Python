from collections import Counter


class Solution():
    """
    https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8

    The new "Avengers" movie has just been released!
    There are a lot of people at the cinema box office standing in a huge line.
    Each of them has a single 100, 50 or 25 dollars bill.
    A "Avengers" ticket costs 25 dollars.

    Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
    Can Vasya sell a ticket to each person and give the change
    if he initially has no money and sells the tickets strictly in the order people follow in the line?
    Return YES, if Vasya can sell a ticket to each person and give the change.
    Otherwise return NO.

    Examples:

    ### Python ###

    tickets([25, 25, 50]) # => YES
    tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
    """

    def __init__(self):
        pass

    def tickets_01(self, people):
        """
        intuitive, bill-set to find
        """

        def isSubList(sublist, baselist):
            c = Counter(sublist)
            for change in c:
                if c[change] > baselist.count(change):
                    return False
            return True

        changes_kept = []
        for cash in people:
            if cash == 25:
                changes_kept.append(cash)
            if cash == 50:
                if 25 in changes_kept:
                    changes_kept.remove(25)
                    changes_kept.append(50)
                else:
                    return 'NO'
            elif cash == 100:
                changes_togive_set = [[25, 50], [25, 25, 25]]
                checklst = [isSubList(changes_togive, changes_kept)
                            for changes_togive in changes_togive_set]
                if True in checklst:
                    for change in changes_togive_set[checklst.index(True)]:
                        changes_kept.remove(change)
                else:
                    return "NO"
        return "YES"

    def tickets_02(self, people):
        """
        intuitive, single-bill to find
        """
        bills_kept = {25: 0, 50: 0, 100: 0}
        for bill in people:
            bill_give = bill - 25
            for bill_ in (50, 25):
                while bill_give >= bill_ and bills_kept[bill_] >= 1:
                    bills_kept[bill_] -= 1
                    bill_give -= bill_

            if bill_give != 0:
                return "NO"

            bills_kept[bill] += 1

        return "YES"


def sets_gen(ticket):
    import random
    bills = [25, 50, 100]
    test_sets = []
    for i in range(1, 100):
        if random.choice((True, False)):
            people = []
            cnt_25 = 0
            cnt_50 = 0
            for j in range(i):
                if cnt_25 >= 3 or (cnt_25 >= 1 and cnt_50 >= 1):
                    bill = random.choice([25, 50, 100])
                elif cnt_25 >= 1:
                    bill = random.choice([25, 50])
                else:
                    bill = 25

                if bill == 25:
                    cnt_25 += 1
                elif bill == 50:
                    cnt_25 -= 1
                    cnt_50 += 1
                else:
                    if cnt_50 >= 1:
                        cnt_50 -= 1
                        cnt_25 -= 1
                    else:
                        cnt_25 -= 3

                people.append(bill)
        else:
            people = [random.choice(bills) for _ in range(i)]
        match = ticket(people)
        test_sets.append((
            (people,),
            match
        ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(1000, prt_docstr=False)
