class Solution():
    """
    https://www.codewars.com/kata/bowling-score-calculator

    Task

        Your task is to write a function for calculating the score of a 10 pin bowling game.
        The input for the function is a list of pins knocked down per roll for one player.
        Output is the player's total score.

    Rules

        General rules

        Rules of bowling in a nutshell:

        A game consists of 10 frames. In each frame the player rolls 1 or 2 balls,
        except for the 10th frame, where the player rolls 2 or 3 balls.
        The total score is the sum of your scores for the 10 frames
        If you knock down fewer than 10 pins with 2 balls, your frame score is the number of pins knocked down
        If you knock down all 10 pins with 2 balls (spare), you score the amount of pins knocked down plus
        a bonus - amount of pins knocked down with the next ball
        If you knock down all 10 pins with 1 ball (strike), you score the amount of pins knocked down plus
        a bonus - amount of pins knocked down with the next 2 balls
        Rules for 10th frame

        As the 10th frame is the last one, in case of spare or strike there will be no next balls for the bonus.
        To account for that:

            if the last frame is a spare, player rolls 1 bonus ball.
            if the last frame is a strike, player rolls 2 bonus balls.
        These bonus balls on 10th frame are only counted as a bonus to the respective spare or strike.

    More information

        http://en.wikipedia.org/wiki/Ten-pin_bowling#Scoring

    Input

        You may assume that the input is always valid. This means:

        input list length is correct
        number of pins knocked out per roll is valid
    """

    def __init__(self):
        pass

    @staticmethod
    def bowling_score_01(rolls):
        """
        intuitive
        """
        ret = 0
        i_frame = 0
        i = 0
        while i_frame < 10:
            # strike
            if rolls[i] == 10:
                ret += 10 + rolls[i + 1] + rolls[i + 2]
                i += 1
            else:
                score = rolls[i] + rolls[i + 1]
                # spare
                if score == 10:
                    ret += 10 + rolls[i + 2]
                else:
                    ret += score
                i += 2
            i_frame += 1
        return ret

    @staticmethod
    def bowling_score_02(rolls):
        """
        recursion
        """

        def recur(i, i_frame):
            if i_frame == 10:
                return sum(rolls[i:])
            if rolls[i] == 10:
                return 10 + rolls[i + 1] + rolls[i + 2] + recur(i + 1, i_frame + 1)
            score = rolls[i] + rolls[i + 1]
            if score == 10:
                return 10 + rolls[i + 2] + recur(i + 2, i_frame + 1)
            return score + recur(i + 2, i_frame + 1)

        return recur(0, 1)

    @staticmethod
    def bowling_score_03(rolls):
        """
        exec
        """
        ldic = {'s': 0, 'rolls': rolls}
        exec('''
s+=sum(rolls[:2+(rolls[0]+rolls[1]>9)])
rolls=rolls[2-(rolls[0]>9):]
''' * 10,
             None,
             ldic
             )
        return ldic['s']


def sets_gen(bowling_score):
    import random
    test_sets = []
    for i in range(1000):
        rolls = []
        for _ in range(9):
            rolls.append(random.randint(0, 10))
            if rolls[-1] < 10:
                rolls.append(random.randint(0, 10 - rolls[-1]))
        rolls.append(random.randint(0, 10))
        if rolls[-1] < 10:
            rolls.append(random.randint(0, 10 - rolls[-1]))
            if rolls[-2] + rolls[-1] == 10:
                rolls.append(random.randint(0, 10))
        else:
            rolls.append(random.randint(0, 10))
            rolls.append(random.randint(0, 10))

        match = bowling_score(rolls)
        test_sets.append((
            (rolls,),
            match
        ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(10, prt_docstr=True)
