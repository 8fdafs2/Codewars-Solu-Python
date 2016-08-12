class Solution():
    def __init__(self):
        self.User = self.User_01

    class User_01():
        def __init__(self):
            self.rank = -8
            self.progress = 0
            self.ranks = [-8, -7, -6, -5, -4, -3, -2, -1,
                          1, 2, 3, 4, 5, 6, 7, 8]


        def inc_progress(self, rank_activity):
            ranks = self.ranks
            rank_acti = ranks.index(rank_activity)
            if self.rank == ranks[-1]:
                return
            rank_self = ranks.index(self.rank)

            if rank_acti > rank_self:
                progress_inc = 10 * ((rank_acti - rank_self) ** 2)
            elif rank_acti == rank_self:
                progress_inc = 3
            elif rank_acti == rank_self - 1:
                progress_inc = 1
            else:
                progress_inc = 0

            self.progress += progress_inc
            while self.progress >= 100:
                self.progress -= 100
                self.rank = ranks[ranks.index(self.rank) + 1]
                if self.rank == ranks[-1]:
                    self.progress = 0


if __name__ == '__main__':
    sol = Solution()
    user = sol.User()

    user.rank = 1
    user.inc_progress(-1)
    print(user.rank, user.progress)
