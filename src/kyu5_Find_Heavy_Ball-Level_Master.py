class Solution():
    def __init__(self):
        self.find_ball = self.find_ball_01

    def find_ball_01(self, scales):

        pan_l, pan_r = [0, 1, 2], [3, 4, 5]
        w = scales.get_weight(pan_l, pan_r)
        if w != 0:
            if w < 0:
                pan_w = pan_l
            elif w > 0:
                pan_w = pan_r
            pan_l, pan_r = pan_w[:1], pan_w[1:2]
            w = scales.get_weight(pan_l, pan_r)
            if w < 0:
                return pan_l[0]
            elif w > 0:
                return pan_r[0]
            return pan_w[2]

        pan_l, pan_r = [6, ], [7, ]
        w = scales.get_weight(pan_l, pan_r)
        if w < 0:
            return pan_l[0]
        return pan_r[0]


if __name__ == '__main__':
    sol = Solution()
